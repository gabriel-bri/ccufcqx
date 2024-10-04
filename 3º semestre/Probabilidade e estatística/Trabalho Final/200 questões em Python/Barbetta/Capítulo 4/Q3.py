# Total de cartas no baralho
total_cartas = 52

# Número de cartas de ouros
cartas_ouros = 13

# Número de figuras (J, Q, K de cada naipe)
figuras = 12

# Número de figuras de ouros
figuras_ouros = 3

# a) Probabilidade de a carta não ser de ouros
prob_nao_ouros = (total_cartas - cartas_ouros) / total_cartas

# b) Probabilidade de ser uma carta de ouros ou uma figura
prob_ouros_ou_figura = (cartas_ouros + figuras - figuras_ouros) / total_cartas

# Resultados
print(f"Probabilidade de a carta não ser de ouros: {prob_nao_ouros:.4f}")
print(f"Probabilidade de ser uma carta de ouros ou uma figura: {prob_ouros_ou_figura:.4f}")
