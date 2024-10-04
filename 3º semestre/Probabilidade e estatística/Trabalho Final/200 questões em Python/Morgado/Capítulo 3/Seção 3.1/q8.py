from itertools import permutations

def permutacoes_sem_letras_iguais_adjacent(s):
    count = 0
    all_permutations = set(permutations(s))
    for perm in all_permutations:
        valid = True
        for i in range(len(perm) - 1):
            if perm[i] == perm[i + 1]:
                valid = False
                break
        if valid:
            count += 1
    return count

# Exemplo com a sequência "AABBCCDD"
sequencia = "AABBCCDD"
resultado = permutacoes_sem_letras_iguais_adjacent(sequencia)
print(f"Número de permutações de '{sequencia}' sem letras iguais adjacentes: {resultado}")
