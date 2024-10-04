import math

def calcular_caixas():
    total_bombons = 30
    tipos_bombons = 8

    bombons_restantes = total_bombons - tipos_bombons
    combinacoes_repetidas = math.comb(bombons_restantes + tipos_bombons - 1, tipos_bombons - 1)

    return combinacoes_repetidas

resultado = calcular_caixas()
print("Número de caixas diferentes:", resultado)
