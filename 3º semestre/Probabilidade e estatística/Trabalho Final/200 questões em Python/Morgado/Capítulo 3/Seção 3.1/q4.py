from math import comb

total_solucoes = comb(12 + 3 - 1, 3 - 1)

def solucoes_mais_que_7(n):
    sol_uma = 3 * comb(n - 8 + 3 - 1, 3 - 1)
    sol_duas = 0
    sol_tres = 0
    
    return sol_uma - sol_duas + sol_tres

sol_com_uma_ou_mais = solucoes_mais_que_7(12)

print("Número de soluções:", sol_com_uma_ou_mais)
