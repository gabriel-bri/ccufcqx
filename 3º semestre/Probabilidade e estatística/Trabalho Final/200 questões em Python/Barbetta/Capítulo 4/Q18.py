# Probabilidades para cada caixa
P_boa_caixa1 = 8 / 10
P_boa_caixa2 = 6 / 10
P_boa_caixa3 = 15 / 20

# a) Probabilidade de todas as peças serem boas
P_boas_todas = P_boa_caixa1 * P_boa_caixa2 * P_boa_caixa3

# Probabilidades de defeito em cada caixa
P_defeito_caixa1 = 2 / 10
P_defeito_caixa2 = 4 / 10
P_defeito_caixa3 = 5 / 20

# b) Probabilidade de peça defeituosa
P_defeito = (1/3) * P_defeito_caixa1 + (1/3) * P_defeito_caixa2 + (1/3) * P_defeito_caixa3

# c) Probabilidade de ter sido escolhida a caixa I, dado que a peça é defeituosa
P_caixa1_dado_defeito = (P_defeito_caixa1 * (1/3)) / P_defeito

# Resultados
print(f"a) Probabilidade de todas as peças serem boas: {P_boas_todas:.4f}")
print(f"b) Probabilidade de a peça ser defeituosa: {P_defeito:.4f}")
print(f"c) Probabilidade de ter sido escolhida a caixa I, dado que a peça é defeituosa: {P_caixa1_dado_defeito:.4f}")
