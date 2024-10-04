# Generalização da Solução: 
# Permutação da distribuição dos números / Número de vértices * número de faces que cada vértice pode exergar 
import permutar as p


print("Item a)\n")

res = p.permutacao(12) // (p.permutacao(6) * p.permutacao(6) * 2)

print(res, "\n")

print("Item b)\n")

res = p.permutacao(12) // (p.permutacao(4) * p.permutacao(4) * p.permutacao(4) * p.permutacao(3))

print(res, "\n")

print("Item c)\n")

res = p.permutacao(12) // (p.permutacao(5) * p.permutacao(7))

print(res, "\n")

print("Item d)\n")

res = p.permutacao(12) // (p.permutacao(2) * p.permutacao(2) * p.permutacao(2) * p.permutacao(2) * p.permutacao(2) * p.permutacao(2) * p.permutacao(6)  )

print(res, "\n")

print("Item e)\n")

res = p.permutacao(12) // (p.permutacao(2) * p.permutacao(2) * p.permutacao(4)**2 * 2**2)

print(res, "\n")
