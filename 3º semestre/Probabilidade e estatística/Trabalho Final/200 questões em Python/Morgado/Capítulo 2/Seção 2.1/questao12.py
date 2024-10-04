def numero_de_colecoes(n_A, n_B, n_C):
    return (n_A + 1) * (n_B + 1) * (n_C + 1) - 1

# Quantidades de exemplares de cada revista
exemplares_A = 5
exemplares_B = 6
exemplares_C = 10

# Calcular o número de coleções não vazias
num_colecoes = numero_de_colecoes(exemplares_A, exemplares_B, exemplares_C)
print("Número de coleções não vazias de revistas possíveis:", num_colecoes)
