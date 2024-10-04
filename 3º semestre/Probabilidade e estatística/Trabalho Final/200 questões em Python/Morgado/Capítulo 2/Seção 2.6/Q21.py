from math import comb

# Número de elementos em cada conjunto
num_elements = 50

# Cálculo das combinações de 3 elementos de A, B ou C
comb_A = comb(num_elements, 3)
comb_B = comb(num_elements, 3)
comb_C = comb(num_elements, 3)

# Soma das combinações
total_comb_ABC = comb_A + comb_B + comb_C

# Cálculo das combinações de 1 elemento de A, 1 de B e 1 de C
comb_ABC = num_elements ** 3

# Soma total
total_sum = total_comb_ABC + comb_ABC

# Exibição do resultado
print(f'O número total de maneiras é: {total_sum}')
