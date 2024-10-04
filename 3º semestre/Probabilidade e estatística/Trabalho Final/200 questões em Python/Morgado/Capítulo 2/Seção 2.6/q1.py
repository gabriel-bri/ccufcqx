from itertools import product

total_units = 3
count = 0

for combination in product(range(total_units + 1), repeat=4):
    if sum(combination) == total_units:
        count += 1
        print("Solução {}: {}".format(count, combination))

print("Total de soluções:", count)
