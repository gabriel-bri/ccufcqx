def soma_divisores(n):
    soma = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            soma += i
    return soma + n

print("a) A soma dos divisores de 720 é:", soma_divisores(720))

def decomposicoes_em_dois_inteiros(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1
    return count // 2

print("b) 720 pode ser decomposto em um produto de dois inteiros positivos de", decomposicoes_em_dois_inteiros(720), "maneiras.")

def decomposicoes_em_tres_inteiros(n):
    count = 0
    for i in range(1, int(n**(1/3)) + 1):
        if n % i == 0:
            for j in range(i, int((n/i)**0.5) + 1):
                if (n / i) % j == 0:
                    count += 1
    return count

print("c) 720 pode ser decomposto em um produto de três inteiros positivos de", decomposicoes_em_tres_inteiros(720), "maneiras.")

print("d) 144 pode ser decomposto em um produto de dois inteiros positivos de", decomposicoes_em_dois_inteiros(144), "maneiras.")
