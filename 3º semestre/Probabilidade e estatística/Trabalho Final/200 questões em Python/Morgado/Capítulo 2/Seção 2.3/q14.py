import permSimples as p 

a = p.permSimples(32, 5)

print(f'a) {a}\n')

# Primeiro e calculado a possibilidade de uma carta ser de determinado grupo, depois multiplica-se pela possibilidade de qual naipe a carta pertence 
# (Numero de Cartas, Numero de Grupos a serem tirados)

b = 8 * p.permSimples(4, 2) * p.permSimples(7,3) * (4 **3)

print(f'b) {b}\n')

c = p.permSimples(8, 2) * (p.permSimples(4, 2) **2 )* 6 * 4

print(f'c) {c}\n')

d = 8 * p.permSimples(4,3) * p.permSimples(7, 2 ) * (4 ** 2)
 
print(f'd) {d}\n')

e = 8 * 1 * 7 * 4

print(f'e) {e}\n')

f = 8 * p.permSimples(4, 3) * 7 * p.permSimples(4, 2)

print(f'f) {f}\n')

g = 4 * (4**5 - 4)

print(f'g) {g}\n')

h = (p.permSimples(8, 5) - 4) * 4

print(f'h) {h}\n')

i = 4 * 4

print(f'i) {i}\n')

j = 4

print(f'j) {j}\n')
