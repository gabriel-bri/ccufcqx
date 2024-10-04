def digitos_diferentes(numero):
    digitos = set(str(numero))
    return len(digitos) == 4

contador = 0

for numero in range(2401, 10000):
    if digitos_diferentes(numero):
        contador += 1

print("Quantidade de números de quatro dígitos maiores que 2400 com todos os dígitos diferentes:", contador)

