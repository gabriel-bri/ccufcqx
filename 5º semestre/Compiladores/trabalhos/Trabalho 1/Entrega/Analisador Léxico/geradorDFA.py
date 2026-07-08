def epsilon_closure(estados):
    closure = set(estados)
    stack = list(estados)
    
    while stack:
        estado = stack.pop()
        if 'epsilon' in estado.transicoes:
            for destino in estado.transicoes['epsilon']:
                if destino not in closure:
                    closure.add(destino)
                    stack.append(destino)
                    
    return frozenset(closure)

def move(estados, simbolo):
    destinos = set()
    for estado in estados:
        if simbolo in estado.transicoes:
            for destino in estado.transicoes[simbolo]:
                destinos.add(destino)
    return destinos

def nfa_para_dfa(nfa, estados_nfa):
    alfabeto = set()
    for e in estados_nfa:
        for sim in e.transicoes.keys():
            if sim != 'epsilon':
                alfabeto.add(sim)
                
    estado_inicial_dfa = epsilon_closure([nfa.estado_inicial])
    
    estados_dfa = [estado_inicial_dfa]
    fila = [estado_inicial_dfa]
    
    transicoes_dfa = {}
    estados_finais_dfa = []
    
    while fila:
        atual_dfa = fila.pop(0)
        transicoes_dfa[atual_dfa] = {}
        
        is_final = False
        token_final = None
        melhor_prioridade = float('inf') 
        
        for e_nfa in atual_dfa:
            if e_nfa.is_final:
                is_final = True
                if e_nfa.prioridade < melhor_prioridade:
                    melhor_prioridade = e_nfa.prioridade
                    token_final = e_nfa.token
                    
        if is_final:
            estados_finais_dfa.append((atual_dfa, token_final))
            
        for sim in alfabeto:
            alvos = move(atual_dfa, sim)
            if not alvos:
                continue
                
            destino_dfa = epsilon_closure(alvos)
            transicoes_dfa[atual_dfa][sim] = destino_dfa
            
            if destino_dfa not in estados_dfa:
                estados_dfa.append(destino_dfa)
                fila.append(destino_dfa)
                
    return estados_dfa, transicoes_dfa, estado_inicial_dfa, estados_finais_dfa


def testar_palavra(palavra, estado_inicial, transicoes, finais):
    estado_atual = estado_inicial
    

    for char in palavra:
        # Se existe um caminho para a letra atual no DFA, ele avanca
        if char in transicoes.get(estado_atual, {}):
            estado_atual = transicoes[estado_atual][char]
        else:
            return f"Erro lexico: '{palavra}' quebrou no caractere '{char}'."
            
    # Chegou ao fim da palavra. Verifica se o estado que parou e final
    for est_final, nome_token in finais:
        if estado_atual == est_final:
            return f"Sucesso! '{palavra}' reconhecido como {nome_token}"
            
    return f"Erro: '{palavra}' parou em um estado nao-final."

def analisar_linha(linha, estado_inicial, transicoes, finais):
    tokens_reconhecidos = []
    i = 0
    while i < len(linha):
        # pula espaços
        if linha[i] == ' ':
            i += 1
            continue
        
        # tenta reconhecer o próximo token a partir de i
        estado_atual = estado_inicial
        ultimo_token = None
        ultimo_avanço = i

        j = i
        while j < len(linha):
            char = linha[j]
            if char in transicoes.get(estado_atual, {}):
                estado_atual = transicoes[estado_atual][char]
                # verifica se chegou em estado final
                for est_final, nome_token in finais:
                    if estado_atual == est_final:
                        ultimo_token = nome_token
                        ultimo_avanço = j + 1
                j += 1
            else:
                break

        if ultimo_token is None:
            return "ERRO"

        tokens_reconhecidos.append(ultimo_token)
        i = ultimo_avanço

    return ' '.join(tokens_reconhecidos)