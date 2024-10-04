from scipy.special import comb

def numero_funcoes_nao_decrescentes(m, n):
    return comb(m + n - 1, n - 1, exact=True)

# Exemplo para m e n
m = 3
n = 2
numero = numero_funcoes_nao_decrescentes(m, n)
print("Número de funções não decrescentes de I{} para I{}: {}".format(m, n, numero))
