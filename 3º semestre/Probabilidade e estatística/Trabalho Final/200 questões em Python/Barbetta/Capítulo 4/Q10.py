from math import comb

# Número total de cartões
total_cartoes = 15

# a) Probabilidade de que os dois cartões sejam da mesma cor
P_mesma_cor = (comb(3, 2) + comb(4, 2) + comb(5, 2) + comb(3, 2)) / comb(total_cartoes, 2)

# b) Probabilidade de que os dois cartões sejam verdes, sabendo-se que são da mesma cor
P_2_verdes = comb(3, 2) / comb(total_cartoes, 2)
P_verdes_cond = P_2_verdes / P_mesma_cor

# Resultados
print(f"a) Probabilidade de que os dois cartões sejam da mesma cor: {P_mesma_cor:.4f} ou {P_mesma_cor}")
print(f"b) Probabilidade de que os dois cartões sejam verdes, sabendo-se que são da mesma cor: {P_verdes_cond:.4f} ou {P_verdes_cond}")
