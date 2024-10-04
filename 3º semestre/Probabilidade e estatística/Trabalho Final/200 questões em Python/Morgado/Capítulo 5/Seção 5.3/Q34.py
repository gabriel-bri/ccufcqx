# Número total de resultados possíveis
total_resultados = 6 * 6

# Número de casos favoráveis
casos_favoraveis = 0
for resultado_pedro in range(1, 7):  # Resultado de Pedro
    casos_favoraveis += (7 - resultado_pedro)  # João pode ter qualquer valor de resultado_pedro até 6

# Probabilidade
probabilidade = casos_favoraveis / total_resultados

print(f"Probabilidade de o resultado de João ser maior ou igual ao resultado de Pedro: {probabilidade:.2f}")
