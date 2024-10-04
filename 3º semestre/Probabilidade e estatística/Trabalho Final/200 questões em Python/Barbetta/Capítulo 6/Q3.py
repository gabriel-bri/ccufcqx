#distribuição triangular
a = 20  # Limite inferior
b = 24  # Limite superior
c = 22  # Valor mais provável (modo)

# a) P(X > 23)
# Como a função densidade é simétrica e linear decrescente após c, calculamos a área da função para X > 23

P_X_gt_23 = ((b - 23)**2) / ((b - a)*(b - c))

# b) E(X) - Esperança (valor esperado)
E_X = (a + b + c) / 3

# c) Var(X) - Variância
Var_X = (a**2 + b**2 + c**2 - a*b - a*c - b*c) / 18

print(P_X_gt_23, E_X, Var_X)
