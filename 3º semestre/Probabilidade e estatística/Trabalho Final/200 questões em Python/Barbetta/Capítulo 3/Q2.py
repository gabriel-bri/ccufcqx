import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados de temperatura (corrigindo a notação de vírgula para ponto)
temperaturas = [
    74.8, 74.0, 74.7, 74.4, 75.9, 73.8, 74.4, 74.8, 76.8, 73.6,
    75.3, 73.4, 74.7, 73.4, 74.2, 76.4, 73.2, 76.5, 75.6, 73.5,
    76.3, 74.1, 75.0, 76.0, 74.7, 76.8, 74.3, 74.9, 77.0, 75.1,
    72.9, 72.9, 74.6, 75.0, 75.1, 74.9, 74.5, 77.1, 74.6, 74.8,
    76.2, 74.7, 76.0, 75.8, 77.3, 75.2, 77.5, 74.7, 73.3, 74.3
]

# Convertendo para DataFrame
df = pd.DataFrame(temperaturas, columns=['Temperatura'])

# Construindo a tabela de frequências
frequencia_absoluta = df['Temperatura'].value_counts().sort_index()
frequencia_relativa = frequencia_absoluta / len(df) * 100
tabela_frequencia = pd.DataFrame({
    'Temperatura (°C)': frequencia_absoluta.index,
    'Frequência Absoluta': frequencia_absoluta.values,
    'Frequência Relativa (%)': frequencia_relativa.values
})

# Adicionando totalizadores na tabela
tabela_frequencia.loc['Total'] = [
    '', 
    tabela_frequencia['Frequência Absoluta'].sum(),
    tabela_frequencia['Frequência Relativa (%)'].sum()
]

# Ajustando a formatação da tabela (formatar apenas valores numéricos)
tabela_frequencia.index = tabela_frequencia.index[:-1].map('{:.1f}'.format).tolist() + ['Total']

# Exibindo a tabela de frequências
print("A - Tabela de Frequências:")
print(tabela_frequencia)

# Plotando o gráfico de barras com dois eixos y
fig, ax1 = plt.subplots(figsize=(12, 6))

# Eixo Y para frequência absoluta
sns.barplot(x=tabela_frequencia.index[:-1], y=tabela_frequencia['Frequência Absoluta'][:-1], color='skyblue', ax=ax1)
ax1.set_xlabel('Temperatura (°C)')
ax1.set_ylabel('Frequência Absoluta', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_title('A - Distribuição das Temperaturas')

# Eixo Y para frequência relativa
ax2 = ax1.twinx()
ax2.plot(tabela_frequencia.index[:-1], tabela_frequencia['Frequência Relativa (%)'][:-1], color='red', marker='o', linestyle='--')
ax2.set_ylabel('Frequência Relativa (%)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Ajustes finais
plt.xticks(rotation=45)
ax1.grid(axis='y')
plt.show()

# Histograma da distribuição das temperaturas
plt.figure(figsize=(10, 6))
sns.histplot(df['Temperatura'], bins=10, kde=False, color='blue')
plt.title('B - Histograma das Temperaturas')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Frequência')
plt.show()

plt.tight_layout()

# Cálculo da distribuição acumulada
df_sorted = df.sort_values('Temperatura').reset_index(drop=True)
df_sorted['Distribuição Acumulada (%)'] = df_sorted.index / len(df_sorted) * 100

# Gráfico da distribuição acumulada
plt.figure(figsize=(10, 6))
plt.plot(df_sorted['Temperatura'], df_sorted['Distribuição Acumulada (%)'], marker='o', linestyle='-')
plt.axhline(y=75, color='r', linestyle='--')
plt.title('C - Distribuição Acumulada das Temperaturas')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Distribuição Acumulada (%)')

# Porcentagem abaixo de 75°C
percentual_abaixo_75 = df_sorted[df_sorted['Temperatura'] < 75]['Distribuição Acumulada (%)'].max()
plt.annotate(f'{percentual_abaixo_75:.1f}% abaixo de 75°C', xy=(75, percentual_abaixo_75), xytext=(76, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12)

plt.show()

def stem_and_leaf_plot(data):
    # Separando ramos e folhas
    ramos = [int(x) for x in np.floor(data)]
    folhas = [int((x - np.floor(x)) * 10) for x in data]
    
    # Construindo o diagrama
    stem_leaf = {}
    for ramo, folha in zip(ramos, folhas):
        if ramo in stem_leaf:
            stem_leaf[ramo].append(folha)
        else:
            stem_leaf[ramo] = [folha]
    
    # Imprimindo o diagrama
    print("D - Diagrama Ramo-e-Folhas:")
    for ramo in sorted(stem_leaf.keys()):
        folhas_str = ' '.join(str(folha) for folha in sorted(stem_leaf[ramo]))
        print(f'{ramo} | {folhas_str}')

# Construindo o diagrama ramo-e-folhas
stem_and_leaf_plot(temperaturas)