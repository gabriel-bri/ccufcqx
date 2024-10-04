from math import floor
#ela remove a parte decimal de um número, 
# retornando o maior inteiro que não é maior que o número original.

def count_multiples(n, low, high):
    return floor(high / n) - floor((low - 1) / n)

low = 1000
high = 10000

A1 = count_multiples(2, low, high)
A2 = count_multiples(3, low, high)
A3 = count_multiples(5, low, high)

A1_A2 = count_multiples(6, low, high)
A1_A3 = count_multiples(10, low, high)
A2_A3 = count_multiples(15, low, high)

A1_A2_A3 = count_multiples(30, low, high)

total_divisible = A1 + A2 + A3 - A1_A2 - A1_A3 - A2_A3 + A1_A2_A3

total_numbers = high - low + 1

not_divisible = total_numbers - total_divisible

print(not_divisible)
