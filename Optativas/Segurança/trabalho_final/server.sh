#!/bin/bash

#Verifica se o script está sendo rodado no modo root, caso contrário
#informa ao usuário que ele precisa de privilégios.
if [[ $USER == "root" ]]; then

        if [[ $1 == "" ]]; then
        
             echo "Instalando o Apache"
             sudo apt update
             sudo apt install apache2
             
        else
             echo -e " --------------------------------------- "
             echo
             sleep 1
             echo -e " \033[31;7;5;107m [+] \033[0m Configurando o servidor..."
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
