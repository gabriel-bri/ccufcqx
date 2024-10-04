import permSimples as p

caso1 = p.permSimples(5, 5) * p.permSimples(7, 1) *  p.permSimples(5, 5) * p.permSimples(7, 1)

caso2 = p.permSimples(5, 4) * p.permSimples(7, 2) * p.permSimples(5, 4) * p.permSimples(7, 2)

caso3 = p.permSimples(5, 3) * p.permSimples(7,3) *  p.permSimples(5, 3) * p.permSimples(7,3)

caso4 = p.permSimples(5, 2) * p.permSimples(7, 4) * p.permSimples(5, 2) * p.permSimples(7, 4)

caso5 = p.permSimples(5, 1) * p.permSimples(7, 5) * p.permSimples(5, 1) * p.permSimples(7, 5)

caso6 = p.permSimples(5, 0) * p.permSimples(7, 6) * p.permSimples(5, 0) * p.permSimples(7, 6)

r = caso1 + caso2 + caso3 + caso4 + caso5 + caso6

print(r)
