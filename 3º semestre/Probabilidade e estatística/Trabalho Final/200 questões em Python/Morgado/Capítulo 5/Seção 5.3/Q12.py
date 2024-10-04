from itertools import product

# Contar o número de combinações que somam 7
total_favoráveis = 0
for dado1, dado2 in product(range(1, 7), repeat=2):
    if dado1 + dado2 == 7:
        total_favoráveis += 1

total_resultados = 6 ** 2
probabilidade = total_favoráveis / total_resultados

print(f"O número total de combinações favoráveis é: {total_favoráveis}")
print(f"A probabilidade de obter uma soma de 7 é: {probabilidade:.4f}")
