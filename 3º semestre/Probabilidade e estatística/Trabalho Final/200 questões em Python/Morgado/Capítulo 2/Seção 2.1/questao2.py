def calcular_gabaritos_possiveis(num_questoes, num_alternativas_por_questao):
    gabaritos_possiveis = num_alternativas_por_questao ** num_questoes
    return gabaritos_possiveis

num_questoes = 10
num_alternativas_por_questao = 5

gabaritos_total = calcular_gabaritos_possiveis(num_questoes, num_alternativas_por_questao)
print("Número de gabaritos possíveis:", gabaritos_total)
