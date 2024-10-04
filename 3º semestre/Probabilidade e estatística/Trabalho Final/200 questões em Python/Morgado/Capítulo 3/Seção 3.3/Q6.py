from math import factorial as f
from math import comb

# Número de permutações das letras não restritas
permutacoes = f(5) // (f(3) * f(1) * f(1))

# Número de formas de escolher 5 espaços dentre 6
escolhas = comb(6, 5)

# Número total de anagramas sem duas letras 'a' consecutivas
total = permutacoes * escolhas

print(f'Número de anagramas com as letras "a" não consecutivas: {total}')
