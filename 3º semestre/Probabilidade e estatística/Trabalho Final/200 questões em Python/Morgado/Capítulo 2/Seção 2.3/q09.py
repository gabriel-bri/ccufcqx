import permSimples as p

# Escolhendo as casas:

f = p.permSimples(7, 2) * p.permSimples(5, 3) * 8 ** 2

# Numero de numeros comecando com zero

z = p.permSimples(6, 2) * p.permSimples(4, 3) * 8

# Excluindo os numeros começando com zero das possibilidades gerais

r = f - z

print(r)
