import person_pb2
import socket

# Conectar ao servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5000))

# Receber os dados
data = client.recv(1024)

# Desserializar os dados
person = person_pb2.Person()
person.ParseFromString(data)

# Verificar os campos
print(f"Recebido: {person.name}, {person.id}, {person.age}, {person.course}, {person.email}")  # Isso deve funcionar
client.close()
