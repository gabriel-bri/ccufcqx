# Q3 - Expressões Disponíveis

import re
import os

SEPARADOR = "-" * 30

_ID_OU_NUM = r'[A-Za-z_]\w*(?:\[[^\]]*\])?|\d+(?:\.\d+)?'

REGEX_ATRIBUICAO = re.compile(
    r'^\s*([A-Za-z_]\w*(?:\[[^\]]*\])?)\s*=\s*(?!=)(.+?)\s*;?\s*$'
)
REGEX_BINOP = re.compile(
    r'^(' + _ID_OU_NUM + r')\s*(<<|>>|<=|>=|==|!=|&&|\|\||\*\*|[+\-*/%&|^<>])\s*('
    + _ID_OU_NUM + r')$'
)
REGEX_UNARIO = re.compile(r'^(-|!|~)\s*(' + _ID_OU_NUM + r')$')


def variavel_base(token):
    correspondencia = re.match(r'^([A-Za-z_]\w*)', token)
    return correspondencia.group(1) if correspondencia else token


def eh_numero(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


def analisar_instrucao(linha_bruta):
    linha = linha_bruta.split('//')[0].strip()
    if not linha:
        return None, None, None

    correspondencia = REGEX_ATRIBUICAO.match(linha)
    if not correspondencia:
        return None, None, None

    lado_esq = correspondencia.group(1)
    lado_dir = correspondencia.group(2).strip()
    variavel_definida = variavel_base(lado_esq)

    binop = REGEX_BINOP.match(lado_dir)
    if binop:
        op1      = binop.group(1)
        operador = binop.group(2)
        op2      = binop.group(3)
        operandos = set()
        if not eh_numero(op1):
            operandos.add(variavel_base(op1))
        if not eh_numero(op2):
            operandos.add(variavel_base(op2))
        texto_expressao = f"{op1} {operador} {op2}"
        return variavel_definida, texto_expressao, operandos

    unario = REGEX_UNARIO.match(lado_dir)
    if unario:
        operador       = unario.group(1)
        operando       = unario.group(2)
        operandos = set()
        if not eh_numero(operando):
            operandos.add(variavel_base(operando))
        texto_expressao = f"{operador}{operando}"
        return variavel_definida, texto_expressao, operandos

    return variavel_definida, None, None


def ler_entrada(texto):
    linhas   = texto.split('\n')
    indice   = 0
    total    = len(linhas)
    ordem    = []
    blocos   = {}

    while indice < total:
        cabecalho = linhas[indice].strip()
        indice += 1

        if cabecalho == '':
            continue

        partes = cabecalho.split()
        if len(partes) < 2:
            continue

        id_bloco        = int(partes[0])
        qtd_instrucoes  = int(partes[1])

        codigo = []
        for _ in range(qtd_instrucoes):
            codigo.append(linhas[indice] if indice < total else '')
            indice += 1

        linha_sucessores = linhas[indice].strip() if indice < total else '0'
        indice += 1
        nums_sucessores  = [int(x) for x in linha_sucessores.split()] if linha_sucessores else [0]
        sucessores       = [] if nums_sucessores == [0] else nums_sucessores

        blocos[id_bloco] = {'codigo': codigo, 'sucessores': sucessores}
        ordem.append(id_bloco)

    return ordem, blocos


def calcular_predecessores(ordem, blocos):
    ids_validos   = set(ordem)
    predecessores = {id_bloco: [] for id_bloco in ordem}

    for id_bloco in ordem:
        for sucessor in blocos[id_bloco]['sucessores']:
            if sucessor in ids_validos:
                predecessores[sucessor].append(id_bloco)

    return predecessores


def calcular_gen_kill(ordem, blocos):
    lista_universo     = []
    operandos_universo = {}

    for id_bloco in ordem:
        for linha_bruta in blocos[id_bloco]['codigo']:
            _, texto_expressao, operandos = analisar_instrucao(linha_bruta)
            if texto_expressao is not None and texto_expressao not in operandos_universo:
                lista_universo.append(texto_expressao)
                operandos_universo[texto_expressao] = operandos

    universo = set(lista_universo)

    # Calcula GEN e KILL de cada bloco
    gen  = {}
    kill = {}

    for id_bloco in ordem:
        conjunto_gen  = set()
        conjunto_kill = set()

        for linha_bruta in blocos[id_bloco]['codigo']:
            variavel_def, texto_expressao, _ = analisar_instrucao(linha_bruta)
            if variavel_def is None:
                continue

            if texto_expressao is not None:
                conjunto_gen.add(texto_expressao)
                conjunto_kill.discard(texto_expressao)

            for expr in lista_universo:
                if variavel_def in operandos_universo[expr]:
                    conjunto_kill.add(expr)
                    conjunto_gen.discard(expr)

        gen[id_bloco]  = conjunto_gen
        kill[id_bloco] = conjunto_kill

    return gen, kill, universo


def analisar_expressoes_disponiveis(ordem, blocos):
    gen, kill, universo = calcular_gen_kill(ordem, blocos)
    predecessores       = calcular_predecessores(ordem, blocos)

    conjunto_in  = {id_bloco: set() for id_bloco in ordem}
    conjunto_out = {
        id_bloco: (set(universo) if predecessores[id_bloco] else set())
        for id_bloco in ordem
    }

    alterou = True
    while alterou:
        alterou = False
        for id_bloco in ordem:

            # IN[B] = interseção dos OUT de todos os predecessores
            if predecessores[id_bloco]:
                novo_in = None
                for pred in predecessores[id_bloco]:
                    if novo_in is None:
                        novo_in = set(conjunto_out[pred])
                    else:
                        novo_in = novo_in & conjunto_out[pred]
            else:
                novo_in = set()  # bloco inicial: nada disponível antes

            # OUT[B] = GEN[B] ∪ (IN[B] - KILL[B])
            novo_out = gen[id_bloco] | (novo_in - kill[id_bloco])

            if novo_in != conjunto_in[id_bloco] or novo_out != conjunto_out[id_bloco]:
                alterou = True

            conjunto_in[id_bloco]  = novo_in
            conjunto_out[id_bloco] = novo_out

    return conjunto_in, conjunto_out


def processar(dados):
    ordem, blocos           = ler_entrada(dados)
    conjunto_in, conjunto_out = analisar_expressoes_disponiveis(ordem, blocos)

    linhas_saida = ["Resultado de Expressoes Disponiveis:"]
    for id_bloco in ordem:
        linhas_saida.append(f"IN[{id_bloco}]  = {sorted(conjunto_in[id_bloco])}")
        linhas_saida.append(f"OUT[{id_bloco}] = {sorted(conjunto_out[id_bloco])}")
        linhas_saida.append(SEPARADOR)

    return "\n".join(linhas_saida)


def main():
    PASTA_ENTRADA = "in"
    PASTA_SAIDA   = "out"

    if not os.path.isdir(PASTA_ENTRADA):
        print(f"Erro: pasta '{PASTA_ENTRADA}' nao encontrada.")
        return

    os.makedirs(PASTA_SAIDA, exist_ok=True)

    for nome_arquivo in os.listdir(PASTA_ENTRADA):
        caminho_entrada = os.path.join(PASTA_ENTRADA, nome_arquivo)
        nome_saida      = os.path.splitext(nome_arquivo)[0] + "_ae.txt"
        caminho_saida   = os.path.join(PASTA_SAIDA, nome_saida)

        with open(caminho_entrada, 'r', encoding='utf-8') as f:
            dados = f.read()

        resultado = processar(dados)

        with open(caminho_saida, 'w', encoding='utf-8') as f:
            f.write(resultado)

        print(f"'{caminho_entrada}' -> '{caminho_saida}'")

if __name__ == "__main__":
    main()