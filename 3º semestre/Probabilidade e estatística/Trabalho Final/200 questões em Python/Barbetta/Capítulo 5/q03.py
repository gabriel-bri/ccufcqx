import matplotlib.pyplot as plt
import numpy as np

# Valores das variáveis discretas (Número de peças)
x = [0, 1, 2, 3]

# Probabilidades correspondentes
probabilidades = [0.216, 0.482, 0.288, 0.064]

# Calculando a distribuição acumulada
cdf = np.cumsum(probabilidades)

# Criando o gráfico da distribuição acumulada
plt.step(x, cdf, where='mid', color='red', linewidth=2)

# Ajustando os rótulos e título
plt.xlabel('Número de peças')
plt.ylabel('Probabilidade acumulada')
plt.title('Função de Distribuição Acumulada (CDF)')

# Exibindo o gráfico
plt.grid(True)
plt.show()

print('0 se x < 0\n0.216 se 0 <= x < 1\n0.698 se 1 <= x < 2\n0.986 se 2 <= x < 3\n1 se x >= 3')