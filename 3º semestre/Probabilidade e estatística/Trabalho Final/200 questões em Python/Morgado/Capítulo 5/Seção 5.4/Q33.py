import math

# Probabilidade de não obter um 6 em um único lançamento
p_not_six = 5 / 6

# Probabilidade desejada de obter pelo menos um 6
p_desired = 0.9

# Encontrar o menor n para que (5/6)^n < 0.1
n = 1
while (p_not_six ** n) >= (1 - p_desired):
    n += 1

print(f"O número mínimo de lançamentos necessário para obter a probabilidade superior a 0,9 é {n}.")
