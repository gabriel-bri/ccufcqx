# Q2 - Reaching Definitions
import os

from longevidade import ler_entrada, extrair_variaveis


class Definicao:
    
    def __init__(self, identificador, variavel, bloco_num, instrucao):
        self.id = identificador          
        self.variavel = variavel         
        self.bloco_num = bloco_num       
        self.instrucao = instrucao

    def __repr__(self):
        return self.id

    def __lt__(self, outro):
        
        return int(self.id[1:]) < int(outro.id[1:])


def numerar_definicoes(blocos):
    
    todas_definicoes = []
    definicoes_por_variavel = {}
    contador = 1

    for num in sorted(blocos.keys()):
        bloco = blocos[num]
        for instrucao in bloco.instrucoes:
            definida, _ = extrair_variaveis(instrucao)
            if definida:
                d = Definicao(f"d{contador}", definida, num, instrucao)
                contador += 1
                todas_definicoes.append(d)
                definicoes_por_variavel.setdefault(definida, []).append(d)

    return todas_definicoes, definicoes_por_variavel


def calcular_gen_kill(blocos, definicoes_por_variavel):
    
    gen = {num: set() for num in blocos}
    kill = {num: set() for num in blocos}

    for num in sorted(blocos.keys()):
        ultima_def_no_bloco = {}  

        
        defs_do_bloco_em_ordem = []
        for lista in definicoes_por_variavel.values():
            for d in lista:
                if d.bloco_num == num:
                    defs_do_bloco_em_ordem.append(d)
        defs_do_bloco_em_ordem.sort()

        for d in defs_do_bloco_em_ordem:
            ultima_def_no_bloco[d.variavel] = d  

        gen[num] = set(ultima_def_no_bloco.values())

        
        k = set()
        for var, d_gen in ultima_def_no_bloco.items():
            for d in definicoes_por_variavel[var]:
                if d != d_gen:
                    k.add(d)
        kill[num] = k

    return gen, kill


def calcular_predecessores(blocos):
    pred = {num: set() for num in blocos}
    for num, bloco in blocos.items():
        for suc in bloco.sucessores:
            if suc in blocos:
                pred[suc].add(num)
    return pred


def analisar_reaching_definitions(blocos, gen, kill):
    
    pred = calcular_predecessores(blocos)

    in_set = {num: set() for num in blocos}
    out_set = {num: set() for num in blocos}

    ordem = sorted(blocos.keys())
    alterou = True
    while alterou:
        alterou = False
        for num in ordem:
            novo_in = set()
            for p in pred[num]:
                novo_in |= out_set[p]

            novo_out = gen[num] | (novo_in - kill[num])

            if novo_in != in_set[num] or novo_out != out_set[num]:
                alterou = True

            in_set[num] = novo_in
            out_set[num] = novo_out

    return in_set, out_set


def processar(dados):
    blocos = ler_entrada(dados)

    _, definicoes_por_variavel = numerar_definicoes(blocos)
    gen, kill = calcular_gen_kill(blocos, definicoes_por_variavel)
    in_set, out_set = analisar_reaching_definitions(blocos, gen, kill)

    return blocos, in_set, out_set


def formatar_saida(blocos, in_set, out_set):
    linhas_saida = ["Resultado de Reaching Definitions:"]
    for num in sorted(blocos.keys()):
        in_str = sorted(in_set[num], key=lambda d: int(d.id[1:]))
        out_str = sorted(out_set[num], key=lambda d: int(d.id[1:]))
        linhas_saida.append(f"IN[{num}]  = {[d.id for d in in_str]}")
        linhas_saida.append(f"OUT[{num}] = {[d.id for d in out_str]}")
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
        nome_saida = os.path.splitext(nome_arquivo)[0] + "_rd.txt"
        caminho_saida = os.path.join(PASTA_SAIDA, nome_saida)

        with open(caminho_entrada, 'r', encoding='utf-8') as f:
            dados = f.read()

        blocos, in_set, out_set = processar(dados)
        resultado = formatar_saida(blocos, in_set, out_set)

        with open(caminho_saida, 'w', encoding='utf-8') as f:
            f.write(resultado)

        print(f"'{caminho_entrada}' -> '{caminho_saida}'")


if __name__ == "__main__":
    main()