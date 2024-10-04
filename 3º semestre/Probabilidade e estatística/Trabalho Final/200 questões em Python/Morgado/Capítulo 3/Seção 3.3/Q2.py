from math import comb

# Total de vértices
n = 10

# Total de triângulos possíveis
total_triangulos = comb(n, 3)

# Triângulos com pelo menos um par de vértices consecutivos
# Há 10 pares de vértices consecutivos
triangulos_com_consecutivos = 10 * 7

# Triângulos válidos (sem vértices consecutivos)
triangulos_validos = total_triangulos - triangulos_com_consecutivos
print(f'O número de triângulos cujos vértices são vértices não consecutivos do decágono é: {triangulos_validos}')
