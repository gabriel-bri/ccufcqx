# Probabilidades dadas
probabilidade_A = 0.02  # 2%
probabilidade_B = 0.01  # 1%
probabilidade_A_e_B = 0.005  # 0,5%

# Cálculo da probabilidade de pelo menos um procedimento falhar
probabilidade_pelo_menos_um = probabilidade_A + probabilidade_B - probabilidade_A_e_B

print(f"Probabilidade de pelo menos um procedimento apresentar resposta insatisfatória: {probabilidade_pelo_menos_um:.4f}")
