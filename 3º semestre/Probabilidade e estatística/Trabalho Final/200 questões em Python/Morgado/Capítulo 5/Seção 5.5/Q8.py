import random

def simula_jogo():
    soma7 = 0
    soma3 = 0
    while soma7 < 2 and soma3 < 3:
        resultado = random.randint(1, 6) + random.randint(1, 6)
        if resultado == 7:
            soma7 += 1
        elif resultado == 3:
            soma3 += 1
    return soma7 == 2

# Número de simulações
simulacoes = 1000000
vitorias = sum(simula_jogo() for _ in range(simulacoes))

# Probabilidade aproximada
probabilidade = vitorias / simulacoes
print(f"A probabilidade de obter duas somas iguais a 7 antes de três somas iguais a 3 é: {probabilidade:.5f}")
