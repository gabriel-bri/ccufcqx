from math import comb

def funcoes_sobrejetoras(n, p):
    if n < p:
        return 0
    resultado = 0
    for k in range(p + 1):
        resultado += (-1)**k * comb(p, k) * (p - k)**n
    return resultado

# Exemplo: número de funções sobrejetoras de um conjunto de 4 elementos para um conjunto de 2 elementos
n = 4
p = 2
print("Número de funções sobrejetoras:", funcoes_sobrejetoras(n, p))
