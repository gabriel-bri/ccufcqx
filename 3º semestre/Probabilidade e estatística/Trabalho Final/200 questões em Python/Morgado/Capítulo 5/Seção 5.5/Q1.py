from math import comb

# Reposição
# Probabilidades
prob_bola_branca = 7 / 10  # Probabilidade de sacar uma bola branca
prob_bola_preta = 3 / 10  # Probabilidade de sacar uma bola preta

# Número de maneiras de obter 2 bolas brancas e 2 bolas pretas
numero_maneiras = comb(4, 2)

# Probabilidade de cada combinação específica
probabilidade_cada_combinacao = (prob_bola_branca**2) * (prob_bola_preta**2)

# Probabilidade total com reposição
probabilidade_total_reposicao = numero_maneiras * probabilidade_cada_combinacao
print(f'Probabilidade de sacar 2 bolas brancas e 2 bolas pretas com reposição: {probabilidade_total_reposicao:.4f}')

# Sem Reposição
# Número de maneiras de escolher 2 bolas brancas de 7 e 2 bolas pretas de 3
maneiras_bolas_brancas = comb(7, 2)
maneiras_bolas_pretas = comb(3, 2)

# Número total de maneiras de escolher 4 bolas de 10
total_maneiras = comb(10, 4)

# Probabilidade total sem reposição
probabilidade_total_sem_reposicao = (maneiras_bolas_brancas * maneiras_bolas_pretas) / total_maneiras
print(f'Probabilidade de sacar 2 bolas brancas e 2 bolas pretas sem reposição: {probabilidade_total_sem_reposicao:.4f}')
