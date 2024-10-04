from math import comb

# Número total de maneiras de dividir 12 pessoas em 3 grupos de 4
total_maneiras = comb(12, 4) * comb(8, 4) * comb(4, 4) // 6

# Número de maneiras de colocar 2 pessoas específicas no mesmo grupo
maneiras_favoraveis = comb(10, 2) * comb(8, 4) * comb(4, 4) // 2

# Probabilidade
probabilidade = maneiras_favoraveis / total_maneiras

print(f"Probabilidade de duas pessoas específicas ficarem no mesmo grupo: {probabilidade:.2f}")
