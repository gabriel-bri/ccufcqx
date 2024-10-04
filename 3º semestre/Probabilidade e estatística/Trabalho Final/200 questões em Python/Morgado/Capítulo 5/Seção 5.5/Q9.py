from scipy.stats import binom

# Parâmetros da distribuição binomial
n = 12  # número de lançamentos
p = 0.4  # probabilidade de obter cara

# Probabilidade de obter exatamente k caras
def probabilidade_mais_provavel(n, p):
    # Calcular a média e arredondar para o inteiro mais próximo
    media = n * p
    k1 = int(media)  # arredondar para baixo
    k2 = k1 + 1  # arredondar para cima
    
    prob_k1 = binom.pmf(k1, n, p)
    prob_k2 = binom.pmf(k2, n, p)
    
    return k1, prob_k1, k2, prob_k2

# Obter o resultado
k1, prob_k1, k2, prob_k2 = probabilidade_mais_provavel(n, p)
print(f"Probabilidade de obter {k1} caras: {prob_k1:.4f}")
print(f"Probabilidade de obter {k2} caras: {prob_k2:.4f}")

# Determinar qual é o valor mais provável
if prob_k1 > prob_k2:
    mais_provavel = k1
else:
    mais_provavel = k2

print(f"O número mais provável de caras obtidas é: {mais_provavel}")
