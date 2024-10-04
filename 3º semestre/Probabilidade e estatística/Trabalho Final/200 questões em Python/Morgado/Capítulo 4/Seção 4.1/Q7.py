def encontrar_tamanho_conjunto(subconjuntos_desejados):
    # Itera sobre valores de n para verificar se 2^n é igual ao número desejado de subconjuntos
    for n in range(1, 21):  # Vamos verificar até n = 20 para garantir uma boa faixa de verificação
        num_subconjuntos = 2 ** n
        if num_subconjuntos == subconjuntos_desejados:
            return n
    return None

# Número de subconjuntos desejados
subconjuntos_desejados = 48
tamanho_conjunto = encontrar_tamanho_conjunto(subconjuntos_desejados)

if tamanho_conjunto is not None:
    print(f'Um conjunto com exatamente {subconjuntos_desejados} subconjuntos deve ter {tamanho_conjunto} elementos.')
else:
    print(f'Não é possível ter um conjunto com exatamente {subconjuntos_desejados} subconjuntos.')
