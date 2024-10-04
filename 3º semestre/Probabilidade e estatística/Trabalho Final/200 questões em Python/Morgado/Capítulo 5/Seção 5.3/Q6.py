import math

# Número total de maneiras de formar dois grupos de 5 pessoas
total_ways = math.comb(10, 5) / 2

# Número de maneiras de formar dois grupos com A e B no mesmo grupo
same_group_ways = math.comb(8, 3)

# Probabilidade
probability = same_group_ways / total_ways

print(f"A probabilidade de que A e B estejam no mesmo grupo é: {probability:.4f}")
