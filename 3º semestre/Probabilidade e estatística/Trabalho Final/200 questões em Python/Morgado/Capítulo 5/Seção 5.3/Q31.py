from math import comb

# Número total de maneiras de escolher 4 pessoas entre 10
total_combinacoes = comb(10, 4)

# Número de maneiras de escolher 3 pessoas entre as 9 restantes
combinacoes_favoraveis = comb(9, 3)

# Probabilidade
probabilidade = combinacoes_favoraveis / total_combinacoes

print(f"Probabilidade de uma pessoa específica ser sorteada: {probabilidade:.2f}")
