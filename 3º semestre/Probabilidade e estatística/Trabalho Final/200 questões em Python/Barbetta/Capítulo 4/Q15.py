# Probabilidades de estar vivo
P_Jose = 0.6
P_Manuel = 0.9

# a) Probabilidade de ambos estarem vivos
P_Ambos_Vivos = P_Jose * P_Manuel

# b) Probabilidade de nenhum estar vivo
P_Jose_Morto = 1 - P_Jose
P_Manuel_Morto = 1 - P_Manuel
P_Nenhum_Vivo = P_Jose_Morto * P_Manuel_Morto

# c) Probabilidade de um estar vivo e o outro estar morto
P_Jose_Vivo_Manuel_Morto = P_Jose * P_Manuel_Morto
P_Jose_Morto_Manuel_Vivo = P_Jose_Morto * P_Manuel
P_Um_Vivo_Outro_Morto = P_Jose_Vivo_Manuel_Morto + P_Jose_Morto_Manuel_Vivo

# Resultados
print(f"a) Probabilidade de ambos estarem vivos: {P_Ambos_Vivos:.2f} ou {P_Ambos_Vivos * 100:.2f}%")
print(f"b) Probabilidade de nenhum estar vivo: {P_Nenhum_Vivo:.2f} ou {P_Nenhum_Vivo * 100:.2f}%")
print(f"c) Probabilidade de um estar vivo e o outro estar morto: {P_Um_Vivo_Outro_Morto:.2f} ou {P_Um_Vivo_Outro_Morto * 100:.2f}%")
