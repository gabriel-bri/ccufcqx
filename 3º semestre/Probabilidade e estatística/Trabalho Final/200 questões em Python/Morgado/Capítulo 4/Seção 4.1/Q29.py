from math import factorial

def combinacao(n, k):
  return factorial(n) // (factorial(k) * factorial(n-k))

# Valores para o exemplo
n = 10

# Calcula e imprime as combinações para todos os valores de p
for p in range(n+1):
  resultado = combinacao(n, p)
  print(f"C({n}, {p}) = {resultado}")