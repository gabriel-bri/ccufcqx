import permSimples as p

# 4 exatamente tres vezes e 8 exatamente duas vezes

caso1 = 12960

# 4 exatamente quatro vezes e 8 duas vezes

caso2 = (p.permSimples(7, 2) * p.permSimples(5, 4) * 8) - p.permSimples(6,4)

#4 figura cinco vezes e 8 duas vezes

caso3 = p.permSimples(7, 5) * p.permSimples(2, 2)

# 4 figura tres vezes e 8 tres vezes

caso4 = (p.permSimples(7, 3) * p.permSimples(4, 3) * 8) - (p.permSimples(6, 3))

print(caso4)

# 4 figura quatro vezes e 8 tres vezes

caso5 = p.permSimples(7, 4)

caso6 = p.permSimples(7, 3)

r = caso1 + caso2 + caso3 + caso4 + caso5 + caso6

print(r)
