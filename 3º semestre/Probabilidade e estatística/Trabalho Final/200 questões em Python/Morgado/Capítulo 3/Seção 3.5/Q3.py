def encontrar_maior_k_quatro_candidatos(num_candidatos, num_alternativas):

  k = 1
  possibilidades = num_alternativas
  while possibilidades * 4 <= num_candidatos:
    k += 1
    possibilidades *= num_alternativas
  return k - 1

# Dados do problema
num_candidatos = 63127
num_alternativas = 5

# Chamando a função e imprimindo o resultado
resultado = encontrar_maior_k_quatro_candidatos(num_candidatos, num_alternativas)
print("O maior valor aproximado de k para 4 candidatos é:", resultado)