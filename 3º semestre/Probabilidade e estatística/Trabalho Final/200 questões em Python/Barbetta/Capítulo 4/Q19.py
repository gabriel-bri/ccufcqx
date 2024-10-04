# Número total de CDs
total_CDs = 1000

# Número de CDs com resistência a arranhão alta
num_resistencia_alta = 800

# Número de CDs aprovados na avaliação das trilhas
num_aprovados = 840

# Número de CDs com resistência alta e aprovados
num_resistencia_alta_e_aprovado = 700

# a) Probabilidade de ter resistência a arranhão alta e ser aprovado na avaliação das trilhas
P_A_inter_B = num_resistencia_alta_e_aprovado / total_CDs

# b) Probabilidade de ter resistência a arranhão alta ou ser aprovado na avaliação das trilhas
P_A = num_resistencia_alta / total_CDs
P_B = num_aprovados / total_CDs
P_A_union_B = P_A + P_B - P_A_inter_B

# c) Probabilidade de ser aprovado na avaliação das trilhas, dado que tem resistência a arranhão alta
P_B_dado_A = P_A_inter_B / P_A

# d) Probabilidade de ter resistência a arranhão alta, dado que foi aprovado na avaliação das trilhas
P_A_dado_B = P_A_inter_B / P_B

# Resultados
print(f"a) Probabilidade de um CD ter resistência a arranhão alta e ser aprovado: {P_A_inter_B:.2f} ou {P_A_inter_B * 100:.2f}%")
print(f"b) Probabilidade de um CD ter resistência a arranhão alta ou ser aprovado: {P_A_union_B:.2f} ou {P_A_union_B * 100:.2f}%")
print(f"c) Probabilidade de um CD ser aprovado, dado que tem resistência a arranhão alta: {P_B_dado_A:.2f} ou {P_B_dado_A * 100:.2f}%")
print(f"d) Probabilidade de um CD ter resistência a arranhão alta, dado que foi aprovado: {P_A_dado_B:.2f} ou {P_A_dado_B * 100:.2f}%")
