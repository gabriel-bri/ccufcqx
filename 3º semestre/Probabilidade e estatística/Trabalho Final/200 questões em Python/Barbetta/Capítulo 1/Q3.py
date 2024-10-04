import math # Importa biblioteca

Dados = [7, 8, 6, 5, 9, 4]

# Cálculo da média
Soma = 0
for Loop in Dados:
    Soma += Loop
    
Media = Soma / len(Dados)

# Cálculo da variância
SomaVariancia = 0
for Loop in Dados:
    SomaVariancia += math.pow((Loop - Media), 2)

print(f'A soma total foi de {Soma} resultando em uma média de {Media}')

Variancia = (SomaVariancia / (len(Dados) - 1))
print(f'A soma dos quadrados da variância foi de {SomaVariancia} resultando em uma variância de {Variancia}')

# Desvio Padrão
print(f'E o desvio padrão foi de {math.sqrt(Variancia):.2f}')