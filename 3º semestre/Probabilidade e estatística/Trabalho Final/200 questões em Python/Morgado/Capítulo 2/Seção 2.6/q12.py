def soma_algarismos(numero):
    soma = 0
    while numero > 0:
        soma += numero % 10
        numero //= 10
    return soma

def contar_numeros_com_soma_6():
    count = 0
    for i in range(1, 100001):
        if soma_algarismos(i) == 6:
            count += 1
    return count

resultado = contar_numeros_com_soma_6()
print("Número de inteiros entre 1 e 100.000 com soma de algarismos igual a 6:", resultado)
