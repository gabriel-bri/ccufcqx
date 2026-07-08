import os
from expressaoRegular import tokens
from geradorNFA import construir_nfa_global, coletar_todos_estados, resetar_contador
from geradorDFA import nfa_para_dfa


def construir_dfa():
    resetar_contador()
    nfa_global = construir_nfa_global(tokens)
    todos_estados_nfa = coletar_todos_estados(nfa_global)
    estados_dfa, transicoes_dfa, estado_inicial_dfa, estados_finais_dfa = nfa_para_dfa(nfa_global, todos_estados_nfa)

    # Transforma os estados finais do DFA num dicionário para busca
    finais_dict = dict(estados_finais_dfa)
    return estado_inicial_dfa, transicoes_dfa, finais_dict


def analisador_lexico(codigo, estado_inicial, transicoes, finais_dict):
    resultado = []
    linhas = codigo.strip().split('\n')

    for linha in linhas:
        if not linha.strip():
            continue

        pos = 0
        tamanho = len(linha)
        tokens_linha = []
        erro_na_linha = False

        while pos < tamanho:
            # Pula espaços em branco
            while pos < tamanho and linha[pos].isspace():
                pos += 1

            if pos == tamanho:
                break

            estado_atual = estado_inicial
            ultimo_estado_final = None
            pos_ultimo_final = -1
            token_encontrado = None

            pos_atual = pos
            while pos_atual < tamanho:
                char = linha[pos_atual]
                
                if char in transicoes.get(estado_atual, {}):
                    estado_atual = transicoes[estado_atual][char]

                    # Verificação robusta se o estado do DFA é final
                    for est_final, nome_token in finais_dict.items():
                        if estado_atual == est_final:
                            ultimo_estado_final = estado_atual
                            pos_ultimo_final = pos_atual
                            token_encontrado = nome_token

                    pos_atual += 1
                else:
                    break

            if ultimo_estado_final is not None:
                lexema = linha[pos:pos_ultimo_final + 1]

                if token_encontrado == "VAR" and len(lexema) > 30:
                    erro_na_linha = True
                    break

                tokens_linha.append(token_encontrado)
                pos = pos_ultimo_final + 1
            else:
                erro_na_linha = True
                break

        if erro_na_linha:
            resultado.append("ERRO")
        else:
            resultado.append(" ".join(tokens_linha))

    return resultado