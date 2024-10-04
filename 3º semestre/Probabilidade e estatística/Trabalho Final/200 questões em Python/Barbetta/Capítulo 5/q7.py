import math as m

def binomial(n, p, x):
    return m.comb(n, x) * (p **x) * (1 - p)**(n - x)


n = 20
p = 0.05

# Para calcularmos a chance de pelo menos um item vir com defeito, basta calcular a distribuição binomial do caso de não vir com nenhum defeito
# e em seguida, tratar de tirar do total(1) esse valor resultante

a = binomial(n, p, 0)

print(f'a) {1 - a}')
#Caso simples onde x=2.

b = binomial(n, p, 2)

print(f'b) {b}')

#Para saber isso, basta pegar do total(1) e subtrair os casos abaixo ou igual ao nosso x
c = binomial(n, p, 0) + binomial(n, p, 1) + binomial(n, p, 2)

print(f'c) {1 - c}')

#Tirar 5% de 20 itens
print(f'd) {1}')

#O que sobrou após a retirada do item d)

print(f'e) {19}')