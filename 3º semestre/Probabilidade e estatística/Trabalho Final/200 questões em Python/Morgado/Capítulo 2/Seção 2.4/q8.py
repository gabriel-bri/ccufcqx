def contar_dados(soma_faces_opostas):
    return len(soma_faces_opostas)

# Para um dado comum de seis faces
soma_faces_opostas_seis_faces = [(1, 6), (2, 5), (3, 4)]
num_dados_seis_faces = contar_dados(soma_faces_opostas_seis_faces)
print("Número de dados diferentes para um dado de seis faces:", num_dados_seis_faces)
