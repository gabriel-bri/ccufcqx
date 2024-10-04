def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

num_mulheres = 5
num_homens = 6
modos = fatorial(num_homens) * fatorial(num_mulheres)

print("Número de modos:", modos)
