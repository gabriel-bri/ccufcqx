import math

lambda_ = 1 / 10000  # Inverso da média

# Tempo (10.000 horas)
t = 10000

# Probabilidade de falha em menos de 10.000 horas
prob_failure = 1 - math.exp(-lambda_ * t)

# Convertendo para percentagem
percent_failure = prob_failure * 100

print(f"A percentagem esperada de componentes que apresentarão falhas em menos de 10.000 horas é {percent_failure:.2f}%")
