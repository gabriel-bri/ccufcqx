import math

lambda_ = 1 / 100  # Taxa de defeitos por metro

# a) Probabilidade de o próximo defeito ocorrer após 120 metros
t_a = 120
prob_no_defect_120 = math.exp(-lambda_ * t_a)

# b) Quantos metros de linha para ter 10% de chance de defeito
prob_defect = 0.10
t_b = -math.log(1 - prob_defect) / lambda_

print(f"a) A probabilidade de o próximo defeito ocorrer após 120 metros é {prob_no_defect_120:.4f}")
print(f"b) O comprimento de linha onde a probabilidade de aparecer algum defeito é de 10% é {t_b:.2f} metros")
