def contar_numeros_com_2():
    contador = 0
    for numero in range(10000, 100000):
        if '2' in str(numero):
            contador += 1
    return contador

def contar_numeros_sem_2():
    contador = 0
    for numero in range(10000, 100000):
        if '2' not in str(numero):
            contador += 1
    return contador

numeros_com_2 = contar_numeros_com_2()
numeros_sem_2 = contar_numeros_sem_2()

print("a) Números de 5 algarismos com o algarismo 2:", numeros_com_2)
print("b) Números de 5 algarismos sem o algarismo 2:", numeros_sem_2)
