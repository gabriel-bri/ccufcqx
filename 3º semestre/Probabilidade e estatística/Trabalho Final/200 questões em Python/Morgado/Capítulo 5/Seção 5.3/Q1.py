import math

def combinacao(n, k):
    return math.comb(n, k)

# Total de peças
total_pecas = 35
pecas_boas = 20
amostra_tamanho = 10

# Número total de maneiras de escolher 10 peças de 35
total_maneiras = combinacao(total_pecas, amostra_tamanho)

# Número de maneiras de escolher 10 peças boas de 20
maneiras_boas = combinacao(pecas_boas, amostra_tamanho)

# Probabilidade de escolher 10 peças boas
probabilidade_todas_boas = maneiras_boas / total_maneiras

# Probabilidade de ao menos uma peça defeituosa
probabilidade_ao_menos_uma_defeito = 1 - probabilidade_todas_boas

print(f"A probabilidade de que ao menos uma peça na amostra seja defeituosa é: {probabilidade_ao_menos_uma_defeito:.4f}")
