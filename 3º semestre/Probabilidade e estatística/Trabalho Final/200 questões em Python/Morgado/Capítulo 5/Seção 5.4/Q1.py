
# Números primos entre 1 e 50
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Números primos ímpares
primos_impares = [p for p in primos if p % 2 != 0]

# Contar o total de números primos e primos ímpares
total_primos = len(primos)
total_primos_impares = len(primos_impares)

# Calcular a probabilidade
probabilidade = total_primos_impares / total_primos
print(f'Probabilidade de que um número seja ímpar dado que é primo: {probabilidade:.4f}')