from itertools import permutations

def contar_arranjos_torres():
    arranjos = permutations(range(8))
    
    # Contar o número de permutações onde nenhuma torre está na mesma linha
    contagem = 0
    for arranjo in arranjos:
        if len(set(arranjo)) == 8:  # Verificar se todas as linhas são diferentes
            contagem += 1
    
    return contagem

num_arranjos = contar_arranjos_torres()
print("Número de modos para arrumar 8 torres em um tabuleiro de xadrez: ", num_arranjos)
