#!/bin/bash

#Verifica se o script está sendo rodado no modo root, caso contrário
#informa ao usuário que ele precisa de privilégios.
if [[ $USER == "root" ]]; then

        #Faz a validação verificando se o IP foi passado, caso contrário
        #retorna um erro exigindo o IP.
        if [[ $1 == "" ]]; then

             #Mensagem de erro.
             echo -e " --------------------------------------- "
             echo
             sleep 1
             echo -e " \033[31;7;5;107m [x] ERRO AO EXECUTAR O SCRIPT \033[0m"
             echo
             echo "  ========================================= "
             echo "  Modo de uso: ./client ip"
             echo "  Exemplo: ./client 192.168.137.128"
             echo "  ========================================= "
             echo
             sleep 1
             echo -e " --------------------------------------- "

             exit 0

        else
             echo -e " --------------------------------------- "
             echo
             sleep 1
             echo -e " \033[31;7;5;107m [+] \033[0m Configurando o Cliente..."
             echo
             sleep 1
             echo -e " --------------------------------------- "


             #Configurando DNS.
             sed -i 's/127.0.0.53/8.8.8.8/g' /etc/resolv.conf
             
             placa1=`ip a | awk -F : '{print $2}' | grep "en"`

             #Cria um cópia de segurança do arquivo original.
             echo "[+] Criando backup do arquivo Netplan."
             cp /etc/netplan/00-installer-config.yaml /etc/netplan/00-installer-config.yaml.bkp

             #Copia o arquivo para a pasta de destino.
             echo "[+] Substituindo arquivo Netplan com as configurações de DNS."
             sed -i 's/ens33/$placa1/g' 00-installer-config.yaml
             cp 00-installer-config.yaml /etc/netplan/

             #Aplica as configurações.
             echo "[+] Aplicando configurações de DNS."
             netplan apply

             #Adiciona rota de comunicação.
             sleep 5
             echo "[+] Configurando o gateway padrão"
             ip route add default via $1

        fi
else
    #Mensagem de erro.
    echo "Você precisa executar este script como root."
fi
