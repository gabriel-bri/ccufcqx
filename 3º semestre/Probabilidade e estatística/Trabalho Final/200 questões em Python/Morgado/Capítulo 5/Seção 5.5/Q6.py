from math import comb

# Probabilidade de recessivo puro
p = 0.25  # Corrigido para ponto decimal

# a) Probabilidade do primeiro filho ser recessivo puro
P_primeiro_recessivo = p

# b) Probabilidade de exatamente 1 dos 4 filhos ser recessivo puro
n = 4
k = 1
P_exatamente_um_recessivo = comb(n, k) * (p**k) * ((1-p)**(n-k))

# Resultados
print(f"a) Probabilidade do primeiro filho ser recessivo puro: {P_primeiro_recessivo:.2f} ou {P_primeiro_recessivo * 100:.2f}%")
print(f"b) Probabilidade de exatamente um dos 4 filhos ser recessivo puro: {P_exatamente_um_recessivo:.5f} ou {P_exatamente_um_recessivo * 100:.2f}%")
