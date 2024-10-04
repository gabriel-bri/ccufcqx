import itertools

def probabilidade_pelo_menos_duas_caras(num_lancamentos, dado_primeiro_lancamento='cara'):
    # Todos os possíveis resultados (exceto o primeiro lançamento fixo)
    resultados_possiveis = itertools.product(['cara', 'coroa'], repeat=num_lancamentos-1)

    # Contador de resultados favoráveis (pelo menos duas caras)
    contador_favoraveis = 0

    for resultado in resultados_possiveis:
        # Adiciona o resultado do primeiro lançamento fixo
        resultado_completo = (dado_primeiro_lancamento,) + resultado

        # Conta se há pelo menos duas caras
        if resultado_completo.count('cara') >= 2:
            contador_favoraveis += 1

    # Espaço amostral (considerando o primeiro lançamento fixo)
    espaço_amostral = 2**(num_lancamentos-1)

    # Probabilidade
    probabilidade = contador_favoraveis / espaço_amostral

    return probabilidade

# Chamando a função para o caso específico
probabilidade = probabilidade_pelo_menos_duas_caras(4, 'cara')
print("A probabilidade de obter pelo menos duas caras, dado que o primeiro lançamento foi cara, é:", probabilidade)