import math

n = 8

# Calculando os S_k, onde S_k é o número de permutações circulares
# que fixam exatamente k pares
S = [math.comb(n, k) * math.factorial(n-k-1) for k in range(n)]

# princípio da inclusão-exclusão
a_0 = sum((-1)**k * S[k] for k in range(n))
a_0 += (-1)**n * 1

print(a_0)
