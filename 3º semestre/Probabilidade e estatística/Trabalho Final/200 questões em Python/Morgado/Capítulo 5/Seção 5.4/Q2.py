import itertools

def probabilidade_caras_maior_coroas(num_lancamentos, dado_primeiro_lancamento='coroa'):
    # Todos os possíveis resultados (exceto o primeiro lançamento fixo)
    resultados_possiveis = itertools.product(['cara', 'coroa'], repeat=num_lancamentos-1)

    # Contador de resultados favoráveis (mais caras que coroas)
    contador_favoraveis = 0

    for resultado in resultados_possiveis:
        # Adiciona o resultado do primeiro lançamento fixo
        resultado_completo = (dado_primeiro_lancamento,) + resultado

        # Conta se o número de caras é maior que o de coroas
        if resultado_completo.count('cara') > resultado_completo.count('coroa'):
            contador_favoraveis += 1

    # Espaço amostral (considerando o primeiro lançamento fixo)
    espaço_amostral = 2**(num_lancamentos-1)

    # Probabilidade
    probabilidade = contador_favoraveis / espaço_amostral

    return probabilidade

# Chamando a função para o caso específico
probabilidade = probabilidade_caras_maior_coroas(6, 'coroa')
print("A probabilidade de obter mais caras que coroas, dado que o primeiro lançamento foi coroa, é:", probabilidade)