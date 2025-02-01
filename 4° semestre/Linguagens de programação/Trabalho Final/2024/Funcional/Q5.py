from functools import reduce

def fatorial_duplo(numero):
    return reduce(lambda x, y: x * y, range(numero, 0, -2))

print(fatorial_duplo(int(input().split()[0])))