def algarismos_distintos(numero):
    algarismos = set(str(numero))
    return len(algarismos) == len(str(numero))

def contar_inteiros_com_algarismos_distintos():
    count = 0
    for num in range(1000, 10000):
        if algarismos_distintos(num):
            count += 1
    return count

total_inteiros = contar_inteiros_com_algarismos_distintos()
print("Número de inteiros entre 1000 e 9999 com algarismos distintos:", total_inteiros)
