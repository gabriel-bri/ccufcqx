from scipy.stats import binom

# Dados do problema
p_defeito = 0.05  # Probabilidade de um item ser defeituoso
n_amostra = 15    # Tamanho da amostra

# Alternativa 1: Valor esperado é simplesmente o valor fixo pago por lote
valor_esperado_alternativa_1 = 100

# Alternativa 2: Cálculo do valor esperado com base na distribuição binomial
# Probabilidades usando a distribuição binomial
P_X_0 = binom.pmf(0, n_amostra, p_defeito)
P_X_1 = binom.pmf(1, n_amostra, p_defeito)
P_X_gt_1 = 1 - P_X_0 - P_X_1

# Valores pagos de acordo com o número de defeitos
valor_0_defeitos = 200
valor_1_defeito = 50
valor_mais_de_1_defeito = 5

# Cálculo do valor esperado para a Alternativa 2
valor_esperado_alternativa_2 = (valor_0_defeitos * P_X_0 +
                                valor_1_defeito * P_X_1 +
                                valor_mais_de_1_defeito * P_X_gt_1)

# Resultados
print(f"Valor esperado da Alternativa 1: R$ {valor_esperado_alternativa_1:.2f}")
print(f"Valor esperado da Alternativa 2: R$ {valor_esperado_alternativa_2:.2f}")
