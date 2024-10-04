def gerar_triangulo_pascais(n_linhas):
    triangulo = [[1]]  # Inicia com a primeira linha

    for i in range(1, n_linhas):
        linha_anterior = triangulo[-1]
        nova_linha = [1]  # Começa com 1
        # Calcula os valores intermediários
        for j in range(1, len(linha_anterior)):
            nova_linha.append(linha_anterior[j - 1] + linha_anterior[j])
        nova_linha.append(1)  # Termina com 1
        triangulo.append(nova_linha)

    return triangulo

def imprimir_triangulo(triangulo):
    for linha in triangulo:
        print(' '.join(map(str, linha)).center(40))  # Ajusta o espaçamento para visualização

# Gerar e imprimir as 7 primeiras linhas
n_linhas = 7
triangulo_pascais = gerar_triangulo_pascais(n_linhas)
imprimir_triangulo(triangulo_pascais)
