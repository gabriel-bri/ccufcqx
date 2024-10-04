total_palavras = 26**5 #total

# Número de palavras sem nenhuma letra A
palavras_sem_A = 25**5

# Número de palavras em que A é a letra inicial
palavras_com_A_inicial = 26**4

# Número de palavras em que A figura, mas não é a letra inicial
palavras_com_A = total_palavras - palavras_sem_A - palavras_com_A_inicial

print("O número de palavras de 5 letras distintas com A, mas não como a letra inicial, é:", palavras_com_A)


