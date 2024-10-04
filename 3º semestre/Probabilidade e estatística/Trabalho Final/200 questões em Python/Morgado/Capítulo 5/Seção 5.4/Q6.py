def probabilidade_urna_ii(p_a, p_b_dado_a, p_b_dado_ii, p_b_dado_iii):
  # Calculando P(B) usando a lei da probabilidade total
  p_b = p_b_dado_a * p_a + p_b_dado_ii * (1 - p_a) + p_b_dado_iii * (1 - p_a)

  # Calculando P(II|B) usando a fórmula de Bayes
  p_ii_dado_b = (p_b_dado_ii * (1 - p_a)) / p_b

  return p_ii_dado_b

# Valores do problema
p_a = 1/3  # Probabilidade de escolher a urna I
p_b_dado_a = 1/3  # Probabilidade de tirar branca da urna I
p_b_dado_ii = 2/3  # Probabilidade de tirar branca da urna II
p_b_dado_iii = 3/5  # Probabilidade de tirar branca da urna III

# Calculando a probabilidade
resultado = probabilidade_urna_ii(p_a, p_b_dado_a, p_b_dado_ii, p_b_dado_iii)
print("Probabilidade de ter escolhido a urna II:", resultado)