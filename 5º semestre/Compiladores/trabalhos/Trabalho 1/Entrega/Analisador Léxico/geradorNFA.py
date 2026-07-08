# Questão 2 – Construção do NFA via Construção de Thompson

class Estado:
    """Representa um estado dentro do NFA."""
    def __init__(self, id_estado):
        self.id = id_estado
        self.transicoes = {}
        self.is_final = False
        self.token = None
        self.prioridade = 0

    def adicionar_transicao(self, simbolo, estado_destino):
        if simbolo not in self.transicoes:
            self.transicoes[simbolo] = []
        self.transicoes[simbolo].append(estado_destino)

    def __repr__(self):
        return f"Estado({self.id}, token={self.token})"


class NFA:
    """NFA com um estado inicial e um estado final."""
    def __init__(self, estado_inicial, estado_final):
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final


class GeradorEstados:
    def __init__(self):
        self._contador = 1

    def novo_estado(self):
        estado = Estado(self._contador)
        self._contador += 1
        return estado

    def resetar(self):
        self._contador = 1


_gerador = GeradorEstados()

def novo_estado():
    return _gerador.novo_estado()

def resetar_contador():
    _gerador.resetar()


# Thompson
def criar_nfa_caractere(caractere):
    """NFA que reconhece exatamente um caractere."""
    ini = novo_estado()
    fin = novo_estado()
    ini.adicionar_transicao(caractere, fin)
    return NFA(ini, fin)

def concatenar_nfa(nfa1, nfa2):
    """nfa1 seguido de nfa2."""
    nfa1.estado_final.adicionar_transicao('epsilon', nfa2.estado_inicial)
    return NFA(nfa1.estado_inicial, nfa2.estado_final)

def unir_nfa(nfa1, nfa2):
    """nfa1 | nfa2."""
    ini = novo_estado()
    fin = novo_estado()
    ini.adicionar_transicao('epsilon', nfa1.estado_inicial)
    ini.adicionar_transicao('epsilon', nfa2.estado_inicial)
    nfa1.estado_final.adicionar_transicao('epsilon', fin)
    nfa2.estado_final.adicionar_transicao('epsilon', fin)
    return NFA(ini, fin)

def fecho_kleene(nfa):
    """nfa* – zero ou mais repetições."""
    ini = novo_estado()
    fin = novo_estado()
    ini.adicionar_transicao('epsilon', nfa.estado_inicial)
    ini.adicionar_transicao('epsilon', fin)
    nfa.estado_final.adicionar_transicao('epsilon', nfa.estado_inicial)
    nfa.estado_final.adicionar_transicao('epsilon', fin)
    return NFA(ini, fin)

def mais_kleene(nfa):
    """nfa+ – um ou mais repetições."""
    ini = novo_estado()
    fin = novo_estado()
    ini.adicionar_transicao('epsilon', nfa.estado_inicial)
    nfa.estado_final.adicionar_transicao('epsilon', nfa.estado_inicial)
    nfa.estado_final.adicionar_transicao('epsilon', fin)
    return NFA(ini, fin)

def opcional_nfa(nfa):
    """nfa? – zero ou um."""
    ini = novo_estado()
    fin = novo_estado()
    ini.adicionar_transicao('epsilon', nfa.estado_inicial)
    ini.adicionar_transicao('epsilon', fin)
    nfa.estado_final.adicionar_transicao('epsilon', fin)
    return NFA(ini, fin)



# REGEX PARA NFA

# Alfabeto da LangC
ALFABETO_LANGC = (
    [chr(c) for c in range(ord('a'), ord('z') + 1)] +
    [chr(c) for c in range(ord('A'), ord('Z') + 1)] +
    [chr(c) for c in range(ord('0'), ord('9') + 1)] +
    list(' \t\n+-*/=><!@#$%&?|_();"')
)


def _expandir_classe(conteudo: str) -> list:
    """Expande o interior de [...] em lista de caracteres, respeitando a-z."""
    chars = []
    i = 0
    while i < len(conteudo):
        if i + 2 < len(conteudo) and conteudo[i + 1] == '-':
            for c in range(ord(conteudo[i]), ord(conteudo[i + 2]) + 1):
                chars.append(chr(c))
            i += 3
        else:
            chars.append(conteudo[i])
            i += 1
    return chars


def _nfa_de_lista_chars(chars: list) -> NFA:
    """Cria NFA correto (Thompson) que aceita qualquer caractere da lista."""
    ini = novo_estado()
    fin = novo_estado()
    
    # Todos os caracteres saem do mesmo estado inicial e vão para o mesmo final
    for c in chars:
        ini.adicionar_transicao(c, fin)
        
    return NFA(ini, fin)


class _ParserRegex:
    def __init__(self, padrao: str):
        self.padrao = padrao
        self.pos = 0

    def _atual(self):
        return self.padrao[self.pos] if self.pos < len(self.padrao) else None

    def _consumir(self, esperado=None):
        c = self._atual()
        if esperado and c != esperado:
            raise ValueError(
                f"Esperava '{esperado}', obteve '{c}' "
                f"na posição {self.pos} de '{self.padrao}'"
            )
        self.pos += 1
        return c

    def parse(self) -> NFA:
        return self._expr()

    def _expr(self) -> NFA:
        resultado = self._termo()
        while self._atual() == '|':
            self._consumir('|')
            resultado = unir_nfa(resultado, self._termo())
        return resultado

    def _termo(self) -> NFA:
        resultado = None
        while self._atual() is not None and self._atual() not in ('|', ')'):
            f = self._fator()
            resultado = f if resultado is None else concatenar_nfa(resultado, f)
        if resultado is None:          # aceita string vazia
            ini = novo_estado()
            fin = novo_estado()
            ini.adicionar_transicao('epsilon', fin)
            resultado = NFA(ini, fin)
        return resultado

    def _fator(self) -> NFA:
        base = self._base()
        op = self._atual()
        if op == '+':
            self._consumir('+')
            return mais_kleene(base)
        if op == '*':
            self._consumir('*')
            return fecho_kleene(base)
        if op == '?':
            self._consumir('?')
            return opcional_nfa(base)
        return base

    def _base(self) -> NFA:
        c = self._atual()

        if c == '(':
            self._consumir('(')
            nfa = self._expr()
            self._consumir(')')
            return nfa

        if c == '[':
            self._consumir('[')
            negacao = False
            if self._atual() == '^':
                negacao = True
                self._consumir('^')
            conteudo = []
            while self._atual() != ']':
                if self._atual() == '\\':
                    self._consumir('\\')
                    conteudo.append(self._consumir())
                else:
                    conteudo.append(self._consumir())
            self._consumir(']')
            chars = _expandir_classe(''.join(conteudo))
            if negacao:
                chars = [ch for ch in ALFABETO_LANGC if ch not in chars]
            return _nfa_de_lista_chars(chars)

        if c == '\\':
            self._consumir('\\')
            return criar_nfa_caractere(self._consumir())

        self._consumir()
        return criar_nfa_caractere(c)


def regex_para_nfa(padrao: str) -> NFA:
    """Converte uma string de expressão regular em um NFA (Thompson)."""
    return _ParserRegex(padrao).parse()



# Junta todos os NFAs de token em um único NFA global
def construir_nfa_global(dicionario_tokens: dict) -> NFA:
    estado_inicial_global = novo_estado()

    for prioridade, (nome_token, padrao) in enumerate(dicionario_tokens.items(), start=1):
        nfa_token = regex_para_nfa(padrao)

        # Liga o estado inicial global a cada NFA via epsilon
        estado_inicial_global.adicionar_transicao('epsilon', nfa_token.estado_inicial)

        # Marca o estado final com o nome e prioridade do token
        nfa_token.estado_final.is_final = True
        nfa_token.estado_final.token = nome_token
        nfa_token.estado_final.prioridade = prioridade

    return NFA(estado_inicial_global, None)

#coleta todos os estados alcançáveis a partir do inicial

def coletar_todos_estados(nfa: NFA) -> list:
    visitados = set()
    fila = [nfa.estado_inicial]
    estados = []
    while fila:
        s = fila.pop()
        if s.id in visitados:
            continue
        visitados.add(s.id)
        estados.append(s)
        for destinos in s.transicoes.values():
            for d in destinos:
                fila.append(d)
    return estados