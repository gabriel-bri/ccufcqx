from math import comb

def count_valid_permutations():
    num_permutations_1 = comb(7, 7) * comb(8, 7)  # Para o primeiro agrupamento
    num_permutations_2 = comb(6, 1) * comb(8, 6)  # Para o segundo agrupamento
    num_permutations_3 = comb(5, 2) * comb(8, 5)  # Para o terceiro agrupamento
    num_permutations_4 = comb(4, 3) * comb(8, 4)  # Para o quarto agrupamento
  
    total_permutations = num_permutations_1 + num_permutations_2 + num_permutations_3 + num_permutations_4
    
    return total_permutations

result = count_valid_permutations()
print("Número de permutações válidas:", result)
