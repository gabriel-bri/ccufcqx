import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# Parâmetros da distribuição uniforme
a = 0
b = 1

# Função densidade de probabilidade
def pdf_uniform(x):
    if 0 <= x <= 1:
        return 1
    else:
        return 0

# Função de distribuição acumulada
def cdf_uniform(x):
    if x < 0:
        return 0
    elif 0 <= x <= 1:
        return x
    else:
        return 1

# Valor esperado
E_X = (a + b) / 2

# Variância
Var_X = (b - a) ** 2 / 12

# Exibindo os resultados
print(f"Valor esperado: {E_X:.2f}")
print(f"Variância: {Var_X:.4f}")

# Plotando a função densidade de probabilidade (f.d.p.)
x = np.linspace(-0.1, 1.1, 500)
pdf_values = np.array([pdf_uniform(val) for val in x])

plt.figure(figsize=(10, 6))
plt.plot(x, pdf_values, label='f.d.p. da Uniforme [0, 1]')
plt.fill_between(x, pdf_values, alpha=0.3)
plt.title('Função Densidade de Probabilidade')
plt.xlabel('x')
plt.ylabel('f_X(x)')
plt.legend()
plt.grid(True)
plt.show()

# Plotando a função de distribuição acumulada (f.d.a.)
x_cdf = np.linspace(-0.1, 1.1, 500)
cdf_values = np.array([cdf_uniform(val) for val in x_cdf])

plt.figure(figsize=(10, 6))
plt.plot(x_cdf, cdf_values, label='f.d.a. da Uniforme [0, 1]', color='orange')
plt.title('Função de Distribuição Acumulada')
plt.xlabel('x')
plt.ylabel('F_X(x)')
plt.legend()
plt.grid(True)
plt.show()
