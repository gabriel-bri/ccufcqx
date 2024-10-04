import math

# Função para calcular combinação
def combinacao(n, r):
    return math.comb(n, r)

# Calcula C(14, 5) e subtrai 1 para remover o caso "00000"
resultado = combinacao(14, 5) - 1

print(f"O número de inteiros entre 1 e 100.000 em que cada dígito é menor ou igual ao seu sucessor é: {resultado}")
