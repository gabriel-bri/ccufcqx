def calcular_modos_iluminacao(n):
    return 2 ** n - 1

# Número de lâmpadas
n_lampadas = 7
resultado = calcular_modos_iluminacao(n_lampadas)
print(f'Número total de modos de iluminar a sala (com pelo menos uma lâmpada acesa): {resultado}')
