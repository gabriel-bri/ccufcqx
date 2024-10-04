def roda_ciranda_duas_juntas(n):
    # de modo que duas delas permaneçam juntas na roda de ciranda
    return 2 * factorial(n - 2)

def roda_ciranda_p_juntas(n, p):
    # de modo que p delas (onde p < n) permaneçam juntas na roda de ciranda
    return factorial(p) * factorial(n - p)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Teste
n = 5
print("Número de maneiras de organizar as crianças de modo que duas delas permaneçam juntas:", roda_ciranda_duas_juntas(n))
p = 1
print(f"Número de maneiras de organizar as crianças de modo que {p} delas permaneçam juntas:", roda_ciranda_p_juntas(n, p))
