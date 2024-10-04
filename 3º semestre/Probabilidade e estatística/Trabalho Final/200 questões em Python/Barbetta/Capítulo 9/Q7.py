import scipy.stats as stats

# Dados fornecidos
variancia_hipotese_nula = 144  # Variância sob H0
variancia_amostral = 64  # Variância amostral
numero_observacoes = 30  # Número de observações

# Grau de liberdade
grau_liberdade = numero_observacoes - 1

# Estatística do teste qui-quadrado
estatistica_Q2 = (grau_liberdade * variancia_amostral) / variancia_hipotese_nula

# Nível de significância
nivel_significancia = 0.05

# Calcula o valor crítico para o teste bicaudal
valor_critico_inferior = stats.chi2.ppf(nivel_significancia / 2, grau_liberdade)
valor_critico_superior = stats.chi2.ppf(1 - nivel_significancia / 2, grau_liberdade)

# Calcula o valor p
valor_p = 2 * min(stats.chi2.cdf(estatistica_Q2, grau_liberdade), 1 - stats.chi2.cdf(estatistica_Q2, grau_liberdade))

# Resultados
print(f"Estatística do teste qui-quadrado (Q^2): {estatistica_Q2:.2f}")
print(f"Valor crítico inferior: {valor_critico_inferior:.2f}")
print(f"Valor crítico superior: {valor_critico_superior:.2f}")
print(f"Valor p: {valor_p:.4f}")

# Conclusão
if valor_p < nivel_significancia:
    print("Rejeitamos a hipótese nula H0. Há evidência de redução na variação da tensão.")
else:
    print("Não rejeitamos a hipótese nula H0. Não há evidência significativa de redução na variação da tensão.")
