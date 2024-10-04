def calcular_combinacoes_presidente_secretario(total_membros):
    opcoes_presidente = total_membros
    opcoes_secretario = total_membros - 1

    total_combinacoes = opcoes_presidente * opcoes_secretario

    return total_combinacoes

total_membros = 12
total_combinacoes_presidente_secretario = calcular_combinacoes_presidente_secretario(total_membros)
print("Número de maneiras diferentes de escolher um presidente e um secretário:", total_combinacoes_presidente_secretario)
