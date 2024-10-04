def total_inteiros(n):
    return 3 ** n

def inteiros_com_todos_digitos(n):
    return 3 ** n - 3 * (2 ** n) + 3

# Exemplo para n = 4
n = 4
total = total_inteiros(n)
com_todos_digitos = inteiros_com_todos_digitos(n)

print(f"Número total de inteiros de {n} dígitos com dígitos no conjunto {{1, 2, 3}}: {total}")
print(f"Número de inteiros de {n} dígitos onde todos os dígitos 1, 2 e 3 aparecem: {com_todos_digitos}")
