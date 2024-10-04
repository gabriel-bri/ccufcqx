# Probabilidade de um homem ser canhoto
p = 0.1

# Número de homens
n = 10

# Probabilidade de nenhum homem ser canhoto
prob_none_canhoto = (1 - p) ** n

# Probabilidade de haver pelo menos um canhoto
prob_pelo_menos_um_canhoto = 1 - prob_none_canhoto

# Exibindo o resultado
print(f"A probabilidade de haver pelo menos um canhoto em um grupo de {n} homens é {prob_pelo_menos_um_canhoto:.4f}")
