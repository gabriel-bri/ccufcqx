from math import comb

# Número total de peças
total_pecas = 28

# Número total de combinações de duas peças
total_combinacoes = comb(total_pecas, 2)

# Número de combinações com números comuns
combinacoes_com_numero_comum = 7 * comb(7, 2)

# Probabilidade
probabilidade = combinacoes_com_numero_comum / total_combinacoes

print(f"Probabilidade de duas peças de dominó terem um número comum: {probabilidade:.4f}")
