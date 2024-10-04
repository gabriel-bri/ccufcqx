def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# a) Com fecho e relógio
modos_a = fatorial(6)
print("a) Número de modos com fecho e relógio:", modos_a)

# b) Com fecho
modos_b = fatorial(6) // 2
print("b) Número de modos com fecho:", modos_b)

# c) Sem fecho e braço em um sentido
modos_c = fatorial(5)
print("c) Número de modos sem fecho e braço em um sentido:", modos_c)

# d) Sem fecho e braço em dois sentidos
modos_d = fatorial(5) // 2
print("d) Número de modos sem fecho e braço em dois sentidos:", modos_d)
