import math

# Definindo a função para calcular combinações
def combinacao(n, k):
    return math.comb(n, k)

# Definindo os valores de n e k
n = 20
k = 4

# Calculando o número de termos
numero_de_termos = combinacao(n + k - 1, k - 1)

# Imprimindo o resultado
print(f"O número de termos distintos no desenvolvimento é: {numero_de_termos}")
