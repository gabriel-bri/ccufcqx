def probabilidade_dama_e_copas():
  total_cartas = 52
  damas = 4
  cartas_de_copas = 13

  prob_dama = damas / total_cartas
  prob_copas_depois_dama = cartas_de_copas / (total_cartas - 1)

  prob_total = prob_dama * prob_copas_depois_dama
  return prob_total

resultado = probabilidade_dama_e_copas()
print("Probabilidade:", resultado)