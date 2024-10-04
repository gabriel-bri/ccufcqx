import matplotlib.pyplot as plt
import numpy as np

# Exemplo de dados (Número de peças)
numeros_de_pecas = [0, 1, 2, 3]

plt.bar(numeros_de_pecas, [0.216, 0.482, 0.288, 0.064], color='red', edgecolor='black',alpha=0.7 )
plt.xlabel('Número de peças')
plt.ylabel('Probabilidade')
plt.title('Histograma de Número de Peças vs. Probabilidade')

# Exibindo o histograma
plt.show()
