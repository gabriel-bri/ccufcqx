def has_distinct_digits(number):
    digits = set(str(number))
    return len(digits) == 3

count = 0

for num in range(100, 1000):
    # Verificar se o número é ímpar e possui três dígitos distintos
    if num % 2 != 0 and has_distinct_digits(num):
        count += 1

print("Número de inteiros ímpares entre 100 e 999 com três dígitos distintos:", count)
