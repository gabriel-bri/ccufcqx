from math import comb

def numero_de_coqueteis(n):
    total_coqueteis = sum(comb(n, k) for k in range(2, n+1))
    return total_coqueteis

# Número de ingredientes
n_ingredientes = 7
resultado = numero_de_coqueteis(n_ingredientes)
print(f'Número total de coquetéis possíveis: {resultado}')
