import math

lambda_ = 0.75  # Taxa de falhas por ano

# Probabilidade de o equipamento não falhar no próximo ano
prob_no_failure = math.exp(-lambda_ * 1)

print(f"A probabilidade de o equipamento não falhar no próximo ano é {prob_no_failure:.4f}")
