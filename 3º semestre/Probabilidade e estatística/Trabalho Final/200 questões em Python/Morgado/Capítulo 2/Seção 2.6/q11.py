import math

def combinacao_completa(n, k):
    return math.factorial(n + k - 1) // (math.factorial(k) * math.factorial(n - 1))

cores = 3
objetos = 6

formas_de_pintar = combinacao_completa(cores, objetos)
print("Quantidade de formas de pintar os seis objetos:", formas_de_pintar)
