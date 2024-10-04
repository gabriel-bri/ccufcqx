def minimo_pessoas_para_5_no_mes(n_meses, min_pessoas_por_mes):
    # Calcula o número mínimo de pessoas para garantir pelo menos min_pessoas_por_mes em um mês
    pessoas = (min_pessoas_por_mes - 1) * n_meses + 1
    return pessoas

# Número de meses no ano e o número mínimo de pessoas desejadas no mesmo mês
n_meses = 12
min_pessoas_por_mes = 5

# Calcula o número mínimo de pessoas
resultado = minimo_pessoas_para_5_no_mes(n_meses, min_pessoas_por_mes)
print(f'O número mínimo de pessoas necessário para garantir que pelo menos {min_pessoas_por_mes} pessoas nasceram no mesmo mês é: {resultado}')
