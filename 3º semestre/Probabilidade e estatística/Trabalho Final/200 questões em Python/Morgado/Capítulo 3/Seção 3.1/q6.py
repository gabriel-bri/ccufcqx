from math import factorial

def permutacoes_restritas():
    total = factorial(6)
    
    # Permutações com 4 na 4ª posição
    perm_4_na_4 = factorial(5)
    
    # Permutações com 6 na 6ª posição
    perm_6_na_6 = factorial(5)
    
    # Permutações com 4 na 4ª posição e 6 na 6ª posição
    perm_4_na_4_e_6_na_6 = factorial(4)
    
    # Aplicando o princípio da inclusão-exclusão
    resultado = total - (perm_4_na_4 + perm_6_na_6 - perm_4_na_4_e_6_na_6)
    
    return resultado

print("Número de permutações onde o 4 não está na 4ª posição e o 6 não está na 6ª posição:", permutacoes_restritas())
