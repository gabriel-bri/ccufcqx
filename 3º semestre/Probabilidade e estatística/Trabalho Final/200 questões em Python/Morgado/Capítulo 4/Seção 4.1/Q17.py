def soma_quadrados(n):
    return n * (n + 1) * (2 * n + 1) // 6

def soma_naturais(n):
    return n * (n + 1) // 2

# Calcula a soma dos quadrados e dos naturais
n1 = 100
n2 = 49
soma_quadrados_100 = soma_quadrados(n1)
soma_quadrados_49 = soma_quadrados(n2)
soma_naturais_100 = soma_naturais(n1)
soma_naturais_49 = soma_naturais(n2)

soma_quadrados_intervalo = soma_quadrados_100 - soma_quadrados_49
soma_naturais_intervalo = soma_naturais_100 - soma_naturais_49

# Soma total
S = soma_quadrados_intervalo + soma_naturais_intervalo
print(f'O valor da soma é: {S}')
