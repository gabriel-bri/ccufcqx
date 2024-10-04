from math import factorial

def numeros_de_cinco_algarismos():
    algarismos = [1, 1, 1, 1, 2, 3]
    
    # Contagem de ocorrências de cada algarismo
    ocorrencias = {1: 4, 2: 1, 3: 1}

    # Número total de algarismos
    total_algarismos = sum(ocorrencias.values())

    # Calcular o número de permutações
    num_permutacoes = factorial(total_algarismos) // (factorial(ocorrencias[1]) * factorial(ocorrencias[2]) * factorial(ocorrencias[3]))
    
    return num_permutacoes

resultado = numeros_de_cinco_algarismos()
print("Número total de números de 5 algarismos:", resultado)
