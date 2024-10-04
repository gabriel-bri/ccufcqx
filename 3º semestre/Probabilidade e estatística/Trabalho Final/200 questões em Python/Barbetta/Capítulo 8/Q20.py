from scipy.stats import chi2

n = 30  # Tamanho da amostra
var_amostra = 64  # Variância da amostra
var_populacao = 144  # Variância populacional sob H0
alpha = 0.05  # Nível de significância

# Calculando a estatística do teste qui-quadrado
gl = n - 1  # Graus de liberdade
Q2 = (gl * var_amostra) / var_populacao

# Calculando o valor crítico para um teste bicaudal
chi2_critical_lower = chi2.ppf(alpha / 2, gl)
chi2_critical_upper = chi2.ppf(1 - alpha / 2, gl)

# Calculando o valor-p
p_value = 1 - chi2.cdf(Q2, gl)

print(Q2, chi2_critical_lower, chi2_critical_upper, p_value)
