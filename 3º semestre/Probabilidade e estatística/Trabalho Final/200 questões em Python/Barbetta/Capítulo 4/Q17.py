# Número de pisos e azulejos
total_pisos = 30
total_azulejos = 40
total_pecas = total_pisos + total_azulejos

# a) Probabilidades de retirar uma peça
P_piso = total_pisos / total_pecas
P_azulejo = total_azulejos / total_pecas

# b) Probabilidade com reposição
P_piso_piso = P_piso * P_piso
P_azulejo_azulejo = P_azulejo * P_azulejo
P_piso_azulejo = P_piso * P_azulejo
P_azulejo_piso = P_azulejo * P_piso
P_um_piso_e_um_azulejo = P_piso_azulejo + P_azulejo_piso

# c) Probabilidade sem reposição
P_piso_piso_sem_reposicao = (total_pisos / total_pecas) * ((total_pisos - 1) / (total_pecas - 1))
P_azulejo_azulejo_sem_reposicao = (total_azulejos / total_pecas) * ((total_azulejos - 1) / (total_pecas - 1))
P_um_piso_e_um_azulejo_sem_reposicao = (total_pisos / total_pecas) * (total_azulejos / (total_pecas - 1)) + (total_azulejos / total_pecas) * (total_pisos / (total_pecas - 1))

# d) Probabilidade de defeito
P_defeito_piso = 0.007
P_defeito_azulejo = 0.015
P_piso_defeito = P_piso * P_defeito_piso
P_azulejo_defeito = P_azulejo * P_defeito_azulejo
P_defeito = P_piso_defeito + P_azulejo_defeito

# e) Probabilidade de ser piso dado que apresentou defeito
P_piso_dado_defeito = P_piso_defeito / P_defeito

# Resultados
print(f"a) Probabilidade de retirar um piso: {P_piso:.4f}")
print(f"   Probabilidade de retirar um azulejo: {P_azulejo:.4f}")

print(f"b) Probabilidade de ambos serem pisos: {P_piso_piso:.4f}")
print(f"   Probabilidade de ambos serem azulejos: {P_azulejo_azulejo:.4f}")
print(f"   Probabilidade de um ser piso e o outro azulejo: {P_um_piso_e_um_azulejo:.4f}")

print(f"c) Probabilidade de ambos serem pisos (sem reposição): {P_piso_piso_sem_reposicao:.4f}")
print(f"   Probabilidade de ambos serem azulejos (sem reposição): {P_azulejo_azulejo_sem_reposicao:.4f}")
print(f"   Probabilidade de um ser piso e o outro azulejo (sem reposição): {P_um_piso_e_um_azulejo_sem_reposicao:.4f}")

print(f"d) Probabilidade de a peça apresentar defeito: {P_defeito:.4f}")

print(f"e) Probabilidade de a peça ser piso dado que apresentou defeito: {P_piso_dado_defeito:.4f}")
