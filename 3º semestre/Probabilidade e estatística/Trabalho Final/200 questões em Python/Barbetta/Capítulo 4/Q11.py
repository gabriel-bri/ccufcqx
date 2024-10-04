# Probabilidades fornecidas
P_A = 0.10
P_B = 0.15
P_C = 0.15
P_D = 0.40
P_E = 0.20

P_Erro_A = 0.01
P_Erro_B = 0.02
P_Erro_C = 0.005
P_Erro_D = 0.02
P_Erro_E = 0.08

# a) Probabilidade de o sistema apresentar erro
P_Erro = (P_A * P_Erro_A) + (P_B * P_Erro_B) + (P_C * P_Erro_C) + (P_D * P_Erro_D) + (P_E * P_Erro_E)

# b) Probabilidade de que o pedido tenha sido feito pelo cliente E, sabendo-se que apresentou erro
P_E_dado_Erro = (P_Erro_E * P_E) / P_Erro

# Resultados
print(f"a) Probabilidade de o sistema apresentar erro: {P_Erro:.5f} ou {P_Erro * 100:.2f}%")
print(f"b) Probabilidade de que o pedido tenha sido feito pelo cliente E, sabendo-se que apresentou erro: {P_E_dado_Erro:.5f} ou {P_E_dado_Erro * 100:.2f}%")
