a = 20  # Limite inferior
b = 24  # Limite superior

# a) P(X > 23)
P_X_gt_23 = (b - 23) / (b - a)

# b) E(X) - Esperança (valor esperado)
E_X = (a + b) / 2

# c) Var(X) - Variância
Var_X = ((b - a) ** 2) / 12

print(P_X_gt_23, E_X, Var_X)
