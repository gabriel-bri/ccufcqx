from math import comb

# Número total de inteiros no intervalo
total_numeros = 50

# Número total de combinações possíveis
total_combinacoes = comb(total_numeros, 2)

# Número de combinações onde ambos os números são positivos
positivos = 29
combinacoes_positivos = comb(positivos, 2)

# Número de combinações onde ambos os números são negativos
negativos = 20
combinacoes_negativos = comb(negativos, 2)

# Número total de combinações com produto positivo
total_combinacoes_positivas = combinacoes_positivos + combinacoes_negativos

# Probabilidade de o produto ser positivo
probabilidade_positivo = total_combinacoes_positivas / total_combinacoes

# Resultados
print(f"Probabilidade de o produto ser positivo: {probabilidade_positivo:.4f} ou {probabilidade_positivo * 100:.2f}%")
