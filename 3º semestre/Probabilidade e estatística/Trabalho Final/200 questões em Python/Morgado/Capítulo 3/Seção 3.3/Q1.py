from math import comb, factorial

# Número total de cadeiras e número de pessoas
total_cadeiras = 15
pessoas = 5

# Cálculo dos casos
caso1 = comb(9, 4)  # Escolher 4 cadeiras entre 12 disponíveis após ocupar a primeira cadeira
caso2 = comb(10, 5)  # Escolher 5 cadeiras entre 14 disponíveis se a primeira cadeira não for ocupada

# Número de permutações das pessoas
permutacoes = factorial(pessoas)

# Número total de maneiras
total_maneiras = (caso1 + caso2) * permutacoes
print(f'O número total de maneiras de colocar {pessoas} pessoas em {total_cadeiras} cadeiras ao redor de uma mesa é: {total_maneiras}')
