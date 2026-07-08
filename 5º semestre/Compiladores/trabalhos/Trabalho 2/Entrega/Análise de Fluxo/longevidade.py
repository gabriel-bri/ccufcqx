# Q1 - Análise de Longevidade
import re
import os

class BlocoBasico:
    def __init__(self, numero):
        self.numero = numero
        self.instrucoes = []
        self.sucessores = []
        self.use = set()
        self.def_ = set()
        self.in_set = set()
        self.out_set = set()


def extrair_variaveis(instrucao):
    if '=' in instrucao:
        lado_esq, lado_dir = instrucao.split('=', 1)
        definida = lado_esq.strip()
        # só pega identificadores (ignora números)
        usadas = set(re.findall(r"[a-zA-Z_]\w*", lado_dir))
    else:
        definida = None
        usadas = set(re.findall(r"[a-zA-Z_]\w*", instrucao))
    return definida, usadas


def calcular_use_def(bloco):
    defs_ate_agora = set()

    for instrucao in bloco.instrucoes:
        definida, usadas = extrair_variaveis(instrucao)

        for var in usadas:
            if var not in defs_ate_agora:
                bloco.use.add(var)

        if definida:
            defs_ate_agora.add(definida)

    bloco.def_ = defs_ate_agora


def analisar_longevidade(blocos):
    ordem = sorted(blocos.keys(), reverse=True)

    alterou = True
    while alterou:
        alterou = False
        for num in ordem:
            bloco = blocos[num]

            novo_out = set()
            for suc in bloco.sucessores:
                if suc in blocos:
                    novo_out |= blocos[suc].in_set

            novo_in = bloco.use | (novo_out - bloco.def_)

            if novo_in != bloco.in_set or novo_out != bloco.out_set:
                alterou = True
                bloco.in_set = novo_in
                bloco.out_set = novo_out


def ler_entrada(dados):
    blocos = {}
    linhas = dados.strip().split('\n')
    i = 0

    while i < len(linhas):
        linha = linhas[i].strip()
        if not linha:
            i += 1
            continue

        partes = linha.split()
        num_bloco = int(partes[0])
        qtd_instrucoes = int(partes[1])
        i += 1

        bloco = BlocoBasico(num_bloco)
        bloco.instrucoes = [linhas[i + k].strip() for k in range(qtd_instrucoes)]
        i += qtd_instrucoes

        sucessores = [int(s) for s in linhas[i].split() if s != '0']
        bloco.sucessores = sucessores
        i += 1

        blocos[num_bloco] = bloco

    return blocos


def processar(dados):
    blocos = ler_entrada(dados)

    for bloco in blocos.values():
        calcular_use_def(bloco)

    analisar_longevidade(blocos)

    linhas_saida = ["Resultado da análise de longevidade:"]
    for num in sorted(blocos.keys()):
        bloco = blocos[num]
        linhas_saida.append(f"IN[{num}]  = {sorted(bloco.in_set)}")
        linhas_saida.append(f"OUT[{num}] = {sorted(bloco.out_set)}")
        linhas_saida.append("-" * 30)

    return "\n".join(linhas_saida)


def main():
    PASTA_ENTRADA = "in"
    PASTA_SAIDA = "out"

    if not os.path.isdir(PASTA_ENTRADA):
        print(f"Erro: pasta '{PASTA_ENTRADA}' nao encontrada.")
        return

    os.makedirs(PASTA_SAIDA, exist_ok=True)

    for nome_arquivo in os.listdir(PASTA_ENTRADA):
        caminho_entrada = os.path.join(PASTA_ENTRADA, nome_arquivo)
        nome_saida = os.path.splitext(nome_arquivo)[0] + "_al.txt"
        caminho_saida = os.path.join(PASTA_SAIDA, nome_saida)

        with open(caminho_entrada, 'r', encoding='utf-8') as f:
            dados = f.read()

        resultado = processar(dados)

        with open(caminho_saida, 'w', encoding='utf-8') as f:
            f.write(resultado)

        print(f"'{caminho_entrada}' -> '{caminho_saida}'")


if __name__ == "__main__":
    main()