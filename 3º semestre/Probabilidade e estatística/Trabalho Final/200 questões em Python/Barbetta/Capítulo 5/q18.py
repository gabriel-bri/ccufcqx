import math as m

def binomial(n, p, x):
    return m.comb(n, x) * (p **x) * (1 - p)**(n - x)

def poisson(e, tal, x):
    return sum((e**(-tal) * tal**i) / m.factorial(i) for i in range(x + 1))

n = 20
p = 0.01

a = binomial(n, p, 0) + binomial(n, p, 1) + binomial(n, p, 2)

e = 2.71828
tal = n * p

b = poisson(e, tal, 2)
print(f'a) {a:.4f}\nb) { b:.4f}')