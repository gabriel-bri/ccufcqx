from math import factorial, comb

# Número de rapazes e moças
rapazes = 12
mocas = 7

# Número de maneiras de arranjar os rapazes
arranjo_rapazes = factorial(rapazes - 1)

# Número de maneiras de escolher as posições para as moças
escolha_posicoes = comb(rapazes, mocas)

# Número de maneiras de distribuir as moças
distribuicao_mocas = factorial(mocas)

# Número total de arranjos
total_arranjos = arranjo_rapazes * escolha_posicoes * distribuicao_mocas

print(f'O número total de modos de arranjar os rapazes e moças é: {total_arranjos}')
