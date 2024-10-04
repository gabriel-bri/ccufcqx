import scipy.stats as stats

# Dados
mu = 5800  # média em kg/cm²
sigma = 180  # desvio padrão em kg/cm²

# Item a) Probabilidade de resistência inferior a 5600 kg/cm²
x_a = 5600
z_a = (x_a - mu) / sigma
prob_a = stats.norm.cdf(z_a)
print(f'Probabilidade de resistência inferior a {x_a} kg/cm²: {prob_a:.4f}')

# Item b) Probabilidade de resistência entre 5600 kg/cm² e 5950 kg/cm²
x_b1 = 5600
x_b2 = 5950
z_b1 = (x_b1 - mu) / sigma
z_b2 = (x_b2 - mu) / sigma
prob_b = stats.norm.cdf(z_b2) - stats.norm.cdf(z_b1)
print(f'Probabilidade de resistência entre {x_b1} kg/cm² e {x_b2} kg/cm²: {prob_b:.4f}')

# Item c) Probabilidade condicional de resistência superior a 6000 kg/cm², dado que já resistiu a 5600 kg/cm²
x_c1 = 5600
x_c2 = 6000
z_c1 = (x_c1 - mu) / sigma
z_c2 = (x_c2 - mu) / sigma
prob_c1 = 1 - stats.norm.cdf(z_c2)  # P(X > 6000)
prob_c2 = 1 - stats.norm.cdf(z_c1)  # P(X > 5600)
prob_conditional = prob_c1 / prob_c2
print(f'Probabilidade condicional de resistência superior a {x_c2} kg/cm², dado que já resistiu a {x_c1} kg/cm²: {prob_conditional:.4f}')

# Item d) Pressão máxima para garantir 95% de probabilidade de resistência
z_d = -1.645
pressure_max = z_d * sigma + mu
print(f'Pressão máxima para garantir 95% de probabilidade de resistência: {pressure_max:.2f} kg/cm²')
