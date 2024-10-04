def combinacao(n, k):
    if 0 <= k <= n:
        num = 1
        den = 1
        for i in range(1, min(k, n - k) + 1):
            num *= n
            den *= i
            n -= 1
        return num // den
    else:
        return 0

# Número de trajetos de comprimento mínimo de A para B
num_trajetos_AB = combinacao(13, 6)

# Número de trajetos de comprimento mínimo de A para B que passam por C
num_trajetos_ABC = combinacao(7, 3) * combinacao(6, 4)

print("a) Número de trajetos de A para B:", num_trajetos_AB)
print("b) Número de trajetos de A para B que passam por C:", num_trajetos_ABC)
