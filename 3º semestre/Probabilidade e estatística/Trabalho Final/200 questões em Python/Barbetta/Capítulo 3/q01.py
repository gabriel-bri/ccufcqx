import matplotlib.pyplot as mp
import numpy as np


a = 'a) É qualitativa, já que trata-se de características que são observadas na forma de categorias e \n não há planos de realizar operações numéricas com tais variáveis'

b = 'b)\nA: Interface\nB: Desempenho\nC: Me. Análise\nD: Me. Custeio\nE: Manutenção\nF: Personalização\nG: Atualização em tempo real\nH: Confiabilidade\nI: Segurança\nJ: Novas Tecnologias'
data = {'A' : 8, 'B': 7, 'C': 7,
        'D': 12, 'E': 2, 'F': 4,
        'G': 3, 'H': 21, 'I': 6,
        'J': 0}

sorted_data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

categories = list(sorted_data.keys())
frequencies = list(sorted_data.values())

# Calculando a porcentagem acumulada
cumulative_percentages = np.cumsum(frequencies) / sum(frequencies) * 100

# Criando o gráfico de barras
fig, ax1 = mp.subplots()

ax1.bar(categories, frequencies, color='blue')
ax1.set_xlabel('Categorias')
ax1.set_ylabel('Frequências', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

mp.xticks(fontsize = 8, rotation = 0, ha = 'right')

# Criando o eixo secundário para a linha da porcentagem acumulada
ax2 = ax1.twinx()
ax2.plot(categories, cumulative_percentages, color='red', marker='o', linestyle='-')
ax2.set_ylabel('Porcentagem Acumulada (%)', color='red')
ax2.tick_params(axis='y', labelcolor='red')


# Exibindo o gráfico
mp.title('Diagrama de Pareto')
mp.show()

print(a)
print(b)