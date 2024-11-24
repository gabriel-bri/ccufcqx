import socket
import person_pb2

def create_person():
    person = person_pb2.Person()
    person.name = "Aluno de Quixadá"
    person.id = 5678
    person.age = 25
    person.course = "Computer Science"
    person.email = "aluno@alu.ufc.br"
    return person.SerializeToString()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))
server.listen(1)
print("Servidor aguardando conexão...")

conn, addr = server.accept()
print(f"Conexão de {addr}")

data = create_person()
conn.sendall(data)
conn.close()
