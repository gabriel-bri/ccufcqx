def probabilidade_sistema():
  # Probabilidade de um componente funcionar
  p_componente_funciona = 0.9

  # Probabilidade de um ramo funcionar (ambos os componentes funcionam)
  p_ramo_funciona = p_componente_funciona ** 2

  # Probabilidade de um ramo não funcionar
  p_ramo_nao_funciona = 1 - p_ramo_funciona

  # Probabilidade de ambos os ramos não funcionarem
  p_ambos_ramos_nao_funcionam = p_ramo_nao_funciona ** 2

  # Probabilidade do sistema funcionar (pelo menos um ramo funciona)
  p_sistema_funciona = 1 - p_ambos_ramos_nao_funcionam

  return p_sistema_funciona

resultado = probabilidade_sistema()
print("A probabilidade do sistema funcionar é:", resultado * 100, "%")