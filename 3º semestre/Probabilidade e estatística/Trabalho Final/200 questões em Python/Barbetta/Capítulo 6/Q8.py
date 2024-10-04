import scipy.stats as stats

# Valores de Z
Z_a = 1.65
Z_c1, Z_c2 = -1, 1
Z_d1, Z_d2 = -2, 2
Z_e1, Z_e2 = -3, 3
Z_f = 6

# a) P(Z > 1.65)
P_a = 1 - stats.norm.cdf(Z_a)

# b) P(Z < 1.65)
P_b = stats.norm.cdf(Z_a)

# c) P(-1 < Z < 1)
P_c = stats.norm.cdf(Z_c2) - stats.norm.cdf(Z_c1)

# d) P(-2 < Z < 2)
P_d = stats.norm.cdf(Z_d2) - stats.norm.cdf(Z_d1)

# e) P(-3 < Z < 3)
P_e = stats.norm.cdf(Z_e2) - stats.norm.cdf(Z_e1)

# f) P(Z > 6)
P_f = 1 - stats.norm.cdf(Z_f)

# g) Valor de z tal que P(-z < Z < z) = 0.90
z_g = stats.norm.ppf((1 + 0.90) / 2)

# h) Valor de z tal que P(-z < Z < z) = 0.99
z_h = stats.norm.ppf((1 + 0.99) / 2)

# Exibindo os resultados com 4 casas decimais
print(f"a) P(Z > 1.65): {P_a:.4f}")
print(f"b) P(Z < 1.65): {P_b:.4f}")
print(f"c) P(-1 < Z < 1): {P_c:.4f}")
print(f"d) P(-2 < Z < 2): {P_d:.4f}")
print(f"e) P(-3 < Z < 3): {P_e:.4f}")
print(f"f) P(Z > 6): {P_f:.4f}")
print(f"g) Valor de z tal que P(-z < Z < z) = 0.90: {z_g:.4f}")
print(f"h) Valor de z tal que P(-z < Z < z) = 0.99: {z_h:.4f}")
