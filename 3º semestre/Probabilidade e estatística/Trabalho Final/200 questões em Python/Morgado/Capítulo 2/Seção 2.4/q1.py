import math

def calcular_permutacao(n):
    return math.factorial(n)

def calcular_numero_de_modos():
    num_meninos = 5
    num_meninas = 5
    
    maneiras_meninas = calcular_permutacao(num_meninas - 1)  
    maneiras_meninos = calcular_permutacao(num_meninos)
    total_modos = maneiras_meninas * maneiras_meninos
    
    return total_modos

numero_de_modos = calcular_numero_de_modos()
print("Número de modos: ", numero_de_modos)
