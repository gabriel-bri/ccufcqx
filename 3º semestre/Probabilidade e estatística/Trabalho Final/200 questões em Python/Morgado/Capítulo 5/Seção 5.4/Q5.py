# Probabilidades individuais
P_A1 = 1000 / 3000
P_A2 = 2000 / 3000
P_D_given_A1 = 0.03
P_D_given_A2 = 0.01

# Probabilidade total de que a peça seja defeituosa
P_D = P_D_given_A1 * P_A1 + P_D_given_A2 * P_A2

# Probabilidade condicional de que a peça tenha sido produzida pela máquina A
P_A1_given_D = (P_D_given_A1 * P_A1) / P_D

# Exibir o resultado
print(f"A probabilidade de que a peça defeituosa tenha sido produzida pela máquina A é {P_A1_given_D:.4f}")
