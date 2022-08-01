#!/bin/bash

#Verifica se o script está sendo rodado no modo root, caso contrário
#informa ao usuário que ele precisa de privilégios.
if [[ $USER == "root" ]]; then

    echo -e " --------------------------------------- "
    echo
    sleep 1
    echo -e "\033[31;7;5;107m[+]\033[0m Configurando o Firewall..."
    echo
    sleep 1
    echo -e " --------------------------------------- "

    #Interface bridge.
    placa1=`ip a | awk -F : '{print $2}' | grep "en" | head -n 1`
    #Interface host-only.
    placa2=`ip a | awk -F : '{print $2}' | grep "en" | head -n 2 | tail -n 1`
    #Interface host-only
    placa3=`ip a | awk -F : '{print $2}' | grep "en" | tail -n 1`

    #Configurando o DNS do firewall
    sed -i 's/127.0.0.53/8.8.8.8/g' /etc/resolv.conf

    #Faz com que as duas placas sejam ativadas.
    echo "[+] Ativando placa 1."
    ip link set $placa1 up
    echo "[+] Ativando placa 2."
    ip link set $placa2 up
    echo "[+] Ativando placa 3."
    ip link set $placa3 up

    #Pacotes adicionais
    echo "[+] Instalando pacotes adicionais."
    sudo apt update
    sudo apt install squid -y
    sudo apt install ipcalc -y

    #Faz com que as placa host-only faça a busca DHCP por IP.
    echo "[+] Realizando requisição por IP na placa 2."
    dhclient $placa2

    echo "[+] Realizando requisição por IP na placa 3."
    dhclient $placa3

    #Ativa o encanmihamento de pacotes.
    echo "[+] Ativando encaminhamento de pacotes."
    echo 1 > /proc/sys/net/ipv4/ip_forward

    #Adiciona uma regra no IPTABLES para a interface bridge.
    echo "[+] Adicionando mascaramento IP."
    iptables -t nat -A POSTROUTING -o $placa1 -j MASQUERADE

    #Bloqueando conexões no iptables.
    echo "[+] Bloqueando conexões no servidor."
    iptables -P INPUT DROP
    iptables -P FORWARD DROP
    iptables -P OUTPUT DROP

    #Liberando conexões SSH.
    echo "[+] Liberando conexão SSH na porta 22."
    iptables -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT
    iptables -A OUTPUT -p tcp -m tcp --sport 22 -j ACCEPT

    #Liberando protocolo ICMP.
    echo "[+] Liberando ping."
    iptables -A INPUT -p icmp -j ACCEPT
    iptables -A OUTPUT -p icmp -j ACCEPT

    #Liberando conexõe DNS.
    echo "[+] Liberando conexões DNS na porta 53."
    iptables -A OUTPUT -p udp --dport 53 -j ACCEPT
    iptables -A INPUT -p udp --sport 53 -j ACCEPT

    ipPlaca1=`ip a | grep "en" | grep "inet" |  awk -F  " " '{print $2}' | head -n 1`
    ipPlaca2=`ip a | grep "en" | grep "inet" |  awk -F  " " '{print $2}' | head -n 2 | tail -n 1`
    ipPlaca3=`ip a | grep "en" | grep "inet" |  awk -F  " " '{print $2}' | tail -n 1`

    redePlaca2=`ipcalc $ipPlaca2 | grep "Network" |  awk -F  " " '{print $2}'`
    redePlaca3=`ipcalc $ipPlaca3 | grep "Network" |  awk -F  " " '{print $2}'`

    echo "[+] Trabalhando em configurações do Squid..."
    iptables -t nat -A PREROUTING -i $placa2 -p tcp -m tcp --dport 80 -j REDIRECT --to-ports 3129
    iptables -t nat -A PREROUTING -i $placa2 -p tcp -m tcp --dport 433 -j REDIRECT --to-ports 3129

    cp squid.conf.original squid.conf

    #Susbtitue a rede que está no arquivo pela rede na qual o script está sendo executado.
    echo -e "acl localnet src $redePlaca2 \n
    acl blockuece url_regex uece \n
    http_access deny localnet blockuece \n
    acl blockufc url_regex ufc \n
    http_access deny localnet blockufc \n
    http_access allow localnet" >> squid.conf

    #Cria um backup do arquivo original do Squid.
    echo "[+] Criando backup das configurações do Squid."
    cp /etc/squid/squid.conf /etc/squid/squid.conf.bkp
    cp squid.conf /etc/squid/squid.conf

    echo "[+] Recarregando arquivos de configuração do Squid."
    sudo invoke-rc.d squid reload

    echo "[+] Reiniciando o Squid..."
    sudo invoke-rc.d squid restart

    echo "Placa $placa1 tem o IP de $ipPlaca1"
    echo "Placa $placa2 tem o IP de $ipPlaca2"
    echo "Placa $placa3 tem o IP de $ipPlaca3"

    #Aplicando configurações de Iptables para o Cliente.
    echo "[+] Aplicando configurações para o Cliente."

    #Permissão do SSH.
    iptables -A FORWARD -s $redePlaca2 -p tcp -m tcp --sport 22 -j ACCEPT
    iptables -A FORWARD -s $redePlaca2 -p tcp -m tcp --dport 22 -j ACCEPT

    #Permissão de HTTP.
    iptables -A FORWARD -s $redePlaca2 -p tcp -m tcp --sport 80 -j ACCEPT
    iptables -A FORWARD -s $redePlaca2 -p tcp -m tcp --dport 80 -j ACCEPT
    iptables -A FORWARD -d $redePlaca2 -p tcp -m tcp --sport 80 -j ACCEPT
    iptables -A FORWARD -d $redePlaca2 -p tcp -m tcp --dport 80 -j ACCEPT
    
    #Permissão de FTP.
    iptables -A FORWARD -s $redePlaca2 -p tcp -m tcp --sport 21 -j ACCEPT
    iptables -A FORWARD -s $redePlaca2 -p tcp -m tcp --dport 21 -j ACCEPT
    iptables -A FORWARD -d $redePlaca2 -p tcp -m tcp --sport 21 -j ACCEPT
    iptables -A FORWARD -d $redePlaca2 -p tcp -m tcp --dport 21 -j ACCEPT
    

    #Permissão de SMTP.
    iptables -A FORWARD -s $redePlaca2 -p tcp -m tcp --sport 25 -j ACCEPT
    iptables -A FORWARD -s $redePlaca2 -p tcp -m tcp --dport 25 -j ACCEPT
    iptables -A FORWARD -d $redePlaca2 -p tcp -m tcp --sport 25 -j ACCEPT
    iptables -A FORWARD -d $redePlaca2 -p tcp -m tcp --dport 25 -j ACCEPT

    #Permissão de DNS.
    iptables -A FORWARD -d $redePlaca2 -p udp -m udp --dport 53 -j ACCEPT
    iptables -A FORWARD -d $redePlaca2 -p udp -m udp --sport 53 -j ACCEPT
    iptables -A FORWARD -s $redePlaca2 -p udp -m udp --dport 53 -j ACCEPT
    iptables -A FORWARD -s $redePlaca2 -p udp -m udp --sport 53 -j ACCEPT

    #Permissão de HTTPS.
    iptables -A FORWARD -d $redePlaca2 -p tcp --dport 443 -j ACCEPT
    iptables -A FORWARD -d $redePlaca2 -p tcp --sport 443 -j ACCEPT
    iptables -A FORWARD -s $redePlaca2 -p tcp --sport 443 -j ACCEPT
    iptables -A FORWARD -s $redePlaca2 -p tcp --dport 443 -j ACCEPT

    #Permissão para o ICMP.
    iptables -A FORWARD -d $redePlaca2 -p icmp -j ACCEPT
    iptables -A FORWARD -s $redePlaca2 -p icmp -j ACCEPT

    #Aplicando configurações para o Servidor.
    echo "Verifique o IP do servidor web e digite ele abaixo:"
    read ipServidor

    echo "[+] Aplicando configurações para o Servidor."
    #Desviando tráfego par a porta 80 do servidor.
    iptables -t nat -A PREROUTING -d $ipPlaca1 -p tcp --dport 80 -j DNAT --to-destination $ipServidor:80

    #Permissão de HTTP.
    iptables -A FORWARD -s $redePlaca3 -p tcp -m tcp --sport 80 -j ACCEPT
    iptables -A FORWARD -s $redePlaca3 -p tcp -m tcp --dport 80 -j ACCEPT
    iptables -A FORWARD -d $redePlaca3 -p tcp -m tcp --sport 80 -j ACCEPT
    iptables -A FORWARD -d $redePlaca3 -p tcp -m tcp --dport 80 -j ACCEPT

    #Permissão de DNS.
    iptables -A FORWARD -d $redePlaca3 -p udp --dport 53 -j ACCEPT
    iptables -A FORWARD -d $redePlaca3 -p udp --sport 53 -j ACCEPT
    iptables -A FORWARD -s $redePlaca3 -p udp --sport 53 -j ACCEPT
    iptables -A FORWARD -s $redePlaca3 -p udp --dport 53 -j ACCEPT

    #Permissão de HTTPS.
    iptables -A FORWARD -d $redePlaca3 -p tcp --dport 443 -j ACCEPT
    iptables -A FORWARD -d $redePlaca3 -p tcp --sport 443 -j ACCEPT
    iptables -A FORWARD -s $redePlaca3 -p tcp --sport 443 -j ACCEPT
    iptables -A FORWARD -s $redePlaca3 -p tcp --dport 443 -j ACCEPT

    #Permissão para o ICMP.
    iptables -A FORWARD -d $redePlaca3 -p icmp -j ACCEPT
    iptables -A FORWARD -s $redePlaca3 -p icmp -j ACCEPT

    echo "[+] Servidor de Firewall configurando com sucesso."
else
    #Mensagem de erro.
    echo "Você precisa executar este script como root."
fi
