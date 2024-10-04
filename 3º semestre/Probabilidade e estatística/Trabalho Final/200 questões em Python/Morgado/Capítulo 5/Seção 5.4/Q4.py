# Definir a probabilidade de eventos individuais
P_A_e_B = 1 / 36  # Probabilidade de obter 3 na primeira jogada e 4 na segunda jogada
P_B = 6 / 36      # Probabilidade de que a soma das duas jogadas seja 7

# Calcular a probabilidade condicional P(A|B)
P_A_dado_B = P_A_e_B / P_B

# Exibir o resultado
print(f"A probabilidade condicional de obter 3 na primeira jogada, sabendo que a soma dos resultados foi 7, é {P_A_dado_B:.4f}")
