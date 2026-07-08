# Questão 1 – Tokens e suas Expressões Regulares para a LangC
 
tokens = {
    # Palavras reservadas (prioridade maior que VAR, pois vêm antes no dict)
    "NUM"       : r"(num)",
    "TEXT"      : r"(text)",
    "BOOL"      : r"(bool)",
    "SHOW"      : r"(show)",
    "TRUE"      : r"(true)",
    "FALSE"     : r"(false)",
 
    # Literais
    "NUM_LIT"   : r"([0-9]+)",
    "CONST"     : r'("[^"]*")',
 
    # Identificador de variável
    "VAR"       : r"([a-zA-Z_][a-zA-Z0-9_]*)",
 
    # Operadores (EQ_EQ antes de EQ para ter prioridade)
    "EQ_EQ"     : r"(==)",
    "EQ"        : r"(=)",
    "ADD"       : r"(\+)",
    "SUB"       : r"(-)",
    "MUL"       : r"(\*)",
    "DIV"       : r"(/)",
    "GT"        : r"(>)",
    "LT"        : r"(<)",
 
    # Delimitadores
    "SEMICOLON" : r"(;)",
    "LPAREN"    : r"(\()",
    "RPAREN"    : r"(\))",
}