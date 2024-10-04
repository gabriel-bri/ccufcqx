# Definindo a função para calcular a soma dos coeficientes
def soma_coeficientes(expoente):
    # Calcula (-1)^expoente
    resultado = (-1) ** expoente
    return resultado

# Definindo o expoente
expoente = 1822

# Calculando a soma dos coeficientes
soma = soma_coeficientes(expoente)

# Imprimindo o resultado
print(f"A soma dos coeficientes é: {soma}")
