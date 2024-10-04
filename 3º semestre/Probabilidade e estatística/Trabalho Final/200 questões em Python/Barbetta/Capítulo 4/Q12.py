# Probabilidades de resolver o problema
P_Joaozinho = 0.5
P_Mariazinha = 0.7

# Probabilidades de não resolver o problema
P_Nao_Joaozinho = 1 - P_Joaozinho
P_Nao_Mariazinha = 1 - P_Mariazinha

# Probabilidade de ambos não resolverem
P_Nao_Resolvido = P_Nao_Joaozinho * P_Nao_Mariazinha

# Probabilidade de pelo menos um resolver
P_Resolvido = 1 - P_Nao_Resolvido

# Resultados
print(f"Probabilidade de o problema ser resolvido: {P_Resolvido:.2f} ou {P_Resolvido * 100:.2f}%")
