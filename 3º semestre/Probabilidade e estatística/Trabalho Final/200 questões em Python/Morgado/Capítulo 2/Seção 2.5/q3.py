import math

def calcular_caminhos(a, b):
    num_caminhos = math.factorial(a + b) // (math.factorial(a) * math.factorial(b))
    return num_caminhos

a = 3
b = 2
caminhos = calcular_caminhos(a, b)
print("O número de caminhos de (0,0) para ({}, {}) é: {}".format(a, b, caminhos))
