import socket as sk
from time import sleep

print("\t[Código Cliente]\nPrática 1 - Redes de Computadores\n")
print("- Conectando ao Servidor")
sleep(1)

ip_adress = sk.gethostname()
print(ip_adress)
porta = 7658

# Criando Socket com familia IPV4 (AF_INET) e Protocolo TCP (SOCK_STREAM)
cliente_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

# Passando uma tupla como parâmetro da função contendo ENDEREÇO e PORTA
cliente_socket.connect((ip_adress, porta))

# Recebendo mensagem do Servidor e imprimindo ao Usuário
mensagem = cliente_socket.recv(1024)
print("Horário: " + mensagem.decode())