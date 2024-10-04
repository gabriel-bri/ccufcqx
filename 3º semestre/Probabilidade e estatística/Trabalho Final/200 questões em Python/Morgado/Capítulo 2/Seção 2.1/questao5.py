from math import factorial

def calcular_modos_pessoas_em_cadeiras(cadeiras, pessoas):
    modos = factorial(cadeiras) // factorial(cadeiras - pessoas)
    return modos

cadeiras = 5
pessoas = 3
modos = calcular_modos_pessoas_em_cadeiras(cadeiras, pessoas)
print("Número de modos diferentes:", modos)
