def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def modos_roda_ciranda(n):
    if n <= 1:
        return 1
    else:
        return fatorial(n - 1)

n = int(input("Digite o número de casais: "))
modos = modos_roda_ciranda(n)
print("Número de modos:", modos)
