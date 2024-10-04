def probabilidade_sistema(p1, p2, p3, p4):
  
  # Probabilidade de um caminho funcionar: 1 - (probabilidade de falhar)
  prob_caminho_superior_funciona = (1 - p1) * (1 - p2)
  prob_caminho_inferior_funciona = (1 - p3) * (1 - p4)

  # Probabilidade de ambos os caminhos falharem
  prob_ambos_caminhos_falham = (1 - prob_caminho_superior_funciona) * (1 - prob_caminho_inferior_funciona)

  # Probabilidade do sistema funcionar
  prob_sistema_funciona = 1 - prob_ambos_caminhos_falham

  return prob_sistema_funciona

# Valores do problema
p1 = 0.01
p2 = 0.02
p3 = 0.04
p4 = 0.03

# Calculando a probabilidade
resultado = probabilidade_sistema(p1, p2, p3, p4)

print("A probabilidade do sistema funcionar é:", resultado * 100, "%")