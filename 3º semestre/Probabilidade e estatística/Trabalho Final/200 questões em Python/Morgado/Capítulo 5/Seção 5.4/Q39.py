from scipy.special import comb

# Dados
N = 1000
n = 20
x = 1

def probabilidade(k):
    return (comb(k, x) * comb(N - k, n - x)) / comb(N, n)

# Calcular para diferentes valores de k
valores_k = range(1, 101)  # Ajuste o intervalo conforme necessário
probabilidades = [probabilidade(k) for k in valores_k]

# Encontrar o valor de k que maximiza a probabilidade
max_probabilidade = max(probabilidades)
k_max = valores_k[probabilidades.index(max_probabilidade)]

print(f"Valor de k que maximiza a probabilidade: {k_max}")
print(f"Probabilidade máxima: {max_probabilidade}")
