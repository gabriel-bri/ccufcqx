import math

def combinacao(n, r):
    return math.comb(n, r)

def calcular_classes_distintas():
    # Total de combinações possíveis de dígitos com 6 dígitos
    total_combinacoes = combinacao(15, 9)
    
    # Ajustar para remover o caso onde todos os dígitos são zero
    total_classes = total_combinacoes - 1
    
    return total_classes

resultado = calcular_classes_distintas()
print(f"O número de classes distintas é: {resultado}")
