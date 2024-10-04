import math

# Dados fornecidos
variancia = 2  # mm^2
desvio_padrao = math.sqrt(variancia)  # mm
nivel_confianca = 0.95
erro_maximo = 0.8  # mm

# Valor crítico z para 95% de confiança
z_alpha_2 = 1.96

# Cálculo do tamanho da amostra
n = (z_alpha_2 * desvio_padrao / erro_maximo) ** 2

# Arredondar para o inteiro mais próximo
n = math.ceil(n)

print(f"Tamanho da amostra necessário: {n}")
