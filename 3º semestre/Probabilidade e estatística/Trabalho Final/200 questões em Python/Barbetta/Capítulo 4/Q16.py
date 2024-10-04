from math import comb

# Total de candidatos
total_engenheiros = 9
total_engenheiras = 6
total_candidatos = total_engenheiros + total_engenheiras

# a) Total de combinações de 2 candidatos
total_combinacoes = comb(total_candidatos, 2)

# b) Combinacoes de 2 homens
combinacoes_homens = comb(total_engenheiros, 2)

# c) Combinacoes de 2 mulheres
combinacoes_mulheres = comb(total_engenheiras, 2)

# Probabilidade de ambos serem do mesmo sexo
prob_mesmo_sexo = (combinacoes_homens + combinacoes_mulheres) / total_combinacoes

# Probabilidade de serem homens dado que ambos são do mesmo sexo
prob_homens_dado_mesmo_sexo = combinacoes_homens / (combinacoes_homens + combinacoes_mulheres)

# Resultados
print(f"b) Probabilidade de que ambos os selecionados sejam do mesmo sexo: {prob_mesmo_sexo:.4f} ou {prob_mesmo_sexo * 100:.2f}%")
print(f"c) Probabilidade de que ambos os selecionados sejam homens, dado que são do mesmo sexo: {prob_homens_dado_mesmo_sexo:.4f} ou {prob_homens_dado_mesmo_sexo * 100:.2f}%")
