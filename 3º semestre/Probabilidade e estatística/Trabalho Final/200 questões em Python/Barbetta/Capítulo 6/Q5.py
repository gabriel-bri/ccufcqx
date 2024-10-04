from scipy.integrate import quad

# Função densidade de probabilidade (PDF)
def pdf(x):
    if 0 < x < 1:
        return x
    elif 1 < x < 2:
        return 2 - x
    else:
        return 0

# Função para integrar a PDF
def integrate_pdf(a, b):
    result, _ = quad(pdf, a, b)
    return result

# a) P(0 < X < 5)
P_0_5 = integrate_pdf(0, 2)

# b) P(0 < X < 1)
P_0_1 = integrate_pdf(0, 1)

# c) P(1 < X < 3/2)
P_1_3_2 = integrate_pdf(1, 1.5)

# d) E(X) (Esperança)
def expectation(x):
    return x * pdf(x)

E_X, _ = quad(expectation, 0, 2)

# e) E(X^2) (Esperança do quadrado)
def expectation_squared(x):
    return x**2 * pdf(x)

E_X2, _ = quad(expectation_squared, 0, 2)

# Variância V(X)
V_X = E_X2 - E_X**2

print(f"a) P(0 < X < 5) = {P_0_5}")
print(f"b) P(0 < X < 1) = {P_0_1}")
print(f"c) P(1 < X < 3/2) = {P_1_3_2}")
print(f"d) E(X) = {E_X}")
print(f"e) V(X) = {V_X}")
