from itertools import product

# Contar o número de combinações que somam 12
total_favoráveis = 0
for dado1, dado2, dado3 in product(range(1, 7), repeat=3):
    if dado1 + dado2 + dado3 == 12:
        total_favoráveis += 1

total_resultados = 6 ** 3
probabilidade = total_favoráveis / total_resultados

print(f"O número total de combinações favoráveis é: {total_favoráveis}")
print(f"A probabilidade de obter uma soma de 12 é: {probabilidade:.4f}")
