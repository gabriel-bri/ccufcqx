import math

def count_solutions():
    total = 0
    for i in range(3, 10):
        total += math.comb(i-1, 2)
    return total

print("Total de soluções inteiras positivas:", count_solutions())
