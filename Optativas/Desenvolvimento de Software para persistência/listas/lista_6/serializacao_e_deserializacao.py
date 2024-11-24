import person_pb2  # Importa o arquivo gerado pelo Protobuf

# Serialização
person = person_pb2.Person()
person.name = "Alice"
person.age = 30
person.email = "alice@example.com"
person.course = "Computer Science"
person.id = 5940

# Converte para binário (serialização)
serialized_data = person.SerializeToString()
print(f"Serialized data: {serialized_data}")

# Desserialização
new_person = person_pb2.Person()
new_person.ParseFromString(serialized_data)

print("\nDeserialized data:")
print(f"Name: {new_person.name}")
print(f"Age: {new_person.age}")
print(f"Email: {new_person.email}")
print(f"Course: {new_person.course}")
print(f"ID: {new_person.id}")