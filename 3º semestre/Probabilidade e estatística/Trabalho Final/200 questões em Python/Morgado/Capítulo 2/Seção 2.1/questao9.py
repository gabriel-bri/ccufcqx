def possui_dois_digitos_iguais(numero):
    digitos = [int(d) for d in str(numero)]
    return len(set(digitos)) < 4

def contar_numeros_com_dois_digitos_iguais():
    contador = 0
    for numero in range(1000, 10000):
        if possui_dois_digitos_iguais(numero):
            contador += 1
    return contador

total = contar_numeros_com_dois_digitos_iguais()
print("Total de números naturais de 4 dígitos com pelo menos dois dígitos iguais:", total)
