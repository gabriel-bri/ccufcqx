import math

# Número de anéis e dedos
n_anéis = 6
n_dedos = 4

# Calcula o número de soluções inteiras e não negativas
combinacoes_dedos = math.comb(n_anéis + n_dedos - 1, n_dedos - 1)

# Calcula o número de permutações dos anéis
permutacoes_aneis = math.factorial(n_anéis)

# Calcula o resultado final
resultado = combinacoes_dedos * permutacoes_aneis

print(f"O número total de maneiras de colocar {n_anéis} anéis diferentes em {n_dedos} dedos é: {resultado}")
