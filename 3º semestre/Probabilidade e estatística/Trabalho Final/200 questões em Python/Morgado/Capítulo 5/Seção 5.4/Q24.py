import math

# Probabilidade de uma pessoa não fazer aniversário hoje
p_not_today = 364 / 365

# Probabilidade desejada de encontrar pelo menos uma pessoa que faz aniversário hoje
p_desired = 0.5

# Encontrar o menor n para que (364/365)^n <= 0.5
n = 1
while (p_not_today ** n) > (1 - p_desired):
    n += 1

print(f"O número mínimo de pessoas necessário para ter uma probabilidade de pelo menos 0,5 de encontrar alguém que faz aniversário hoje é {n}.")
