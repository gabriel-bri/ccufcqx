from itertools import combinations

def contar_numeros_diferentes(numeros):
    produtos = set()
    for r in range(1, len(numeros) + 1):
        for comb in combinations(numeros, r):
            produto = 1
            for num in comb:
                produto *= num
            produtos.add(produto)
    return len(produtos)

numeros = [1, 5, 6, 7, 7, 9, 9, 9]

total_numeros_diferentes = contar_numeros_diferentes(numeros)
print("Número de números diferentes que podem ser formados:", total_numeros_diferentes)
