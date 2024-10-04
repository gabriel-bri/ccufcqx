import math

lambda_ = 1 / 10000  # Inverso da média

# Probabilidade acumulada
prob_acumulada = 0.25

# Calculando o tempo após o qual 25% dos componentes terão falhado
t = -math.log(1 - prob_acumulada) / lambda_

print(f"O tempo após o qual 25% dos componentes terão falhado é {t:.2f} horas")
