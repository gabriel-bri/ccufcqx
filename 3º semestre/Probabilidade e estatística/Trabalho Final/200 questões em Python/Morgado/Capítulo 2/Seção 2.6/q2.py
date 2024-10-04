def count_solutions():
    total = 0
    for x in range(6):
        for y in range(6-x):
            for z in range(6-x-y):
                for w in range(6-x-y-z):
                    t = 5 - (x + y + z + w)
                    if t >= 0:
                        total += 1
    return total

print("Total de soluções:", count_solutions())
