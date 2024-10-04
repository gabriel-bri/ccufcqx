import math

def calcular_caminhos(a, b, c):
    num_caminhos = math.factorial(a + b + c) // (math.factorial(a) * math.factorial(b) * math.factorial(c))
    return num_caminhos

# Teste
a = 2
b = 3
c = 2
caminhos = calcular_caminhos(a, b, c)
print("O número de caminhos de (0, 0, 0) para ({}, {}, {}) é: {}".format(a, b, c, caminhos))
