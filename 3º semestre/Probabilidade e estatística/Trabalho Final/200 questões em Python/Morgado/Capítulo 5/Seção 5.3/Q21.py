from math import comb

# Total de arranjos possíveis
total_arranjos = comb(12, 4)

# Arranjos com 4 vagas vazias consecutivas
arranjos_consecutivos = 9

# Arranjos com 4 vagas vazias não consecutivas
arranjos_nao_consecutivos = comb(9, 4)

# Probabilidades
probabilidade_consecutivos = arranjos_consecutivos / total_arranjos
probabilidade_nao_consecutivos = arranjos_nao_consecutivos / total_arranjos

print(f"Probabilidade de vagas vazias serem consecutivas: {probabilidade_consecutivos:.4f}")
print(f"Probabilidade de não haver duas vagas vazias consecutivas: {probabilidade_nao_consecutivos:.4f}")
