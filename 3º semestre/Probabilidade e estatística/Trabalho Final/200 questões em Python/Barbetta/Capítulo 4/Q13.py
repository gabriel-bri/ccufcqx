# Probabilidades de falha dos componentes
P_Falha_1 = 0.1
P_Falha_2 = 0.2

# Probabilidades de funcionamento dos componentes
P_Funciona_1 = 1 - P_Falha_1
P_Funciona_2 = 1 - P_Falha_2

# a) Probabilidade de o sistema funcionar em série
P_Sistema_Serie = P_Funciona_1 * P_Funciona_2

# b) Probabilidade de o sistema funcionar em paralelo
P_Ambos_Falham = P_Falha_1 * P_Falha_2
P_Sistema_Paralelo = 1 - P_Ambos_Falham

# Resultados
print(f"a) Probabilidade de o sistema funcionar em série: {P_Sistema_Serie:.2f} ou {P_Sistema_Serie * 100:.2f}%")
print(f"b) Probabilidade de o sistema funcionar em paralelo: {P_Sistema_Paralelo:.2f} ou {P_Sistema_Paralelo * 100:.2f}%")
