from math import factorial

def numeros_de_sete_digitos():
    algarismos = [1, 3, 6, 6, 6, 8, 8]
    
    # Números começando com 6
    numeros_comecando_com_6 = factorial(6) // (factorial(2) * factorial(2))
    
    # Números começando com 8
    numeros_comecando_com_8 = factorial(6) // factorial(3)

    total_numeros = numeros_comecando_com_6 + numeros_comecando_com_8
    
    return total_numeros

resultado = numeros_de_sete_digitos()
print("Número total de números de 7 dígitos:", resultado)
