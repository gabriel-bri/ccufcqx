import pandas as pd

# Criando um dicionário com os dados da tabela
data = {'Tipo_Leite': ['B', 'C', 'UHT'],
        'Dentro_Especificacoes': [500, 4500, 1500],
        'Fora_Especificacoes': [30, 270, 50]}

# Criando um DataFrame a partir do dicionário
df = pd.DataFrame(data)

# Calculando o total de pacotes
df['Total'] = df['Dentro_Especificacoes'] + df['Fora_Especificacoes']

# Calculando o total geral
total_pacotes = df['Total'].sum()

# Calculando as probabilidades
prob_dentro = df['Dentro_Especificacoes'].sum() / total_pacotes
prob_B = df['Total'][0] / total_pacotes
prob_D_e_B = df['Dentro_Especificacoes'][0] / total_pacotes
prob_D_dado_B = prob_D_e_B / prob_B
prob_B_dado_D = prob_D_e_B / prob_dentro

# Imprimindo os resultados
print("Probabilidade de um pacote estar dentro das especificações:", prob_dentro)
print("Probabilidade de um pacote ser do tipo B:", prob_B)
print("Probabilidade de um pacote estar dentro das especificações e ser do tipo B:", prob_D_e_B)
print("Probabilidade de um pacote estar dentro das especificações dado que é do tipo B:", prob_D_dado_B)
print("Probabilidade de um pacote ser do tipo B dado que está dentro das especificações:", prob_B_dado_D)