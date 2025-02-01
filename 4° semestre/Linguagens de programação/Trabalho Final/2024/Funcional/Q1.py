from functools import reduce

def mutiplicar_elementos(numeros):
    return reduce(lambda x, y: x * y, numeros)

print(mutiplicar_elementos(list(map(int, input().split()))))