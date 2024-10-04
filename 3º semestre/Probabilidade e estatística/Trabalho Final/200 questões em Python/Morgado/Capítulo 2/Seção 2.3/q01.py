import permSimples as p

a = p.permSimples(8, 3) * p.permSimples(5,3)
print(f'a) {a} \n')


caso1 = p.permSimples(7,3) * p.permSimples(4,3)

caso2 = p.permSimples(7,2) * p.permSimples(4,3)

caso3 = p.permSimples(7,3) * p.permSimples(4,2)

b = caso1 + caso2 + caso3

print(f'b) {b}\n')
