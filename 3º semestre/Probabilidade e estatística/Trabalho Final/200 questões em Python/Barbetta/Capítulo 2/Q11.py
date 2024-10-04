import numpy as np

# Valores para o nível alto (+)
valores_A_plus = np.array([458.75, 449.50, 463.75, 466.00, 449.50, 452.75, 469.00, 471.50])
valores_B_plus = np.array([446.75, 447.75, 455.50, 448.25, 449.50, 452.75, 469.00, 471.50])
valores_C_plus = np.array([454.25, 456.75, 455.50, 448.25, 463.75, 466.00, 469.00, 471.50])
valores_D_plus = np.array([454.25, 456.75, 446.75, 447.75, 458.75, 449.50, 469.00, 471.50])
valores_E_plus = np.array([433.00, 456.75, 447.75, 448.25, 449.50, 466.00, 452.75, 471.50])
valores_F_plus = np.array([433.00, 454.25, 446.75, 448.25, 449.50, 463.75, 449.50, 471.50])

# Cálculos para o nível alto (+)
soma_A_plus = np.sum(valores_A_plus)
media_A_plus = soma_A_plus / len(valores_A_plus)

soma_B_plus = np.sum(valores_B_plus)
media_B_plus = soma_B_plus / len(valores_B_plus)

soma_C_plus = np.sum(valores_C_plus)
media_C_plus = soma_C_plus / len(valores_C_plus)

soma_D_plus = np.sum(valores_D_plus)
media_D_plus = soma_D_plus / len(valores_D_plus)

soma_E_plus = np.sum(valores_E_plus)
media_E_plus = soma_E_plus / len(valores_E_plus)

soma_F_plus = np.sum(valores_F_plus)
media_F_plus = soma_F_plus / len(valores_F_plus)

print(f'Soma e média dos valores para A(+): Soma = {soma_A_plus:.2f}, Média = {media_A_plus:.2f}')
print(f'Soma e média dos valores para B(+): Soma = {soma_B_plus:.2f}, Média = {media_B_plus:.2f}')
print(f'Soma e média dos valores para C(+): Soma = {soma_C_plus:.2f}, Média = {media_C_plus:.2f}')
print(f'Soma e média dos valores para D(+): Soma = {soma_D_plus:.2f}, Média = {media_D_plus:.2f}')
print(f'Soma e média dos valores para E(+): Soma = {soma_E_plus:.2f}, Média = {media_E_plus:.2f}')
print(f'Soma e média dos valores para F(+): Soma = {soma_F_plus:.2f}, Média = {media_F_plus:.2f}')

# Valores para o nível baixo (-)
valores_A_minus = np.array([429.25, 433.00, 454.25, 456.75, 446.75, 447.75, 455.50, 448.25])
valores_B_minus = np.array([429.25, 433.00, 454.25, 456.75, 458.75, 449.50, 463.75, 466.00])
valores_C_minus = np.array([429.25, 433.00, 446.75, 447.75, 458.75, 449.50, 449.50, 452.75])
valores_D_minus = np.array([429.25, 433.00, 455.50, 448.25, 463.75, 466.00, 449.50, 452.75])
valores_E_minus = np.array([429.25, 454.25, 446.75, 455.50, 458.75, 463.75, 449.50, 469.00])
valores_F_minus = np.array([429.25, 456.75, 447.75, 455.50, 458.75, 466.00, 452.75, 469.00])

# Cálculos para o nível baixo (-)
soma_A_minus = np.sum(valores_A_minus)
media_A_minus = soma_A_minus / len(valores_A_minus)

soma_B_minus = np.sum(valores_B_minus)
media_B_minus = soma_B_minus / len(valores_B_minus)

soma_C_minus = np.sum(valores_C_minus)
media_C_minus = soma_C_minus / len(valores_C_minus)

soma_D_minus = np.sum(valores_D_minus)
media_D_minus = soma_D_minus / len(valores_D_minus)

soma_E_minus = np.sum(valores_E_minus)
media_E_minus = soma_E_minus / len(valores_E_minus)

soma_F_minus = np.sum(valores_F_minus)
media_F_minus = soma_F_minus / len(valores_F_minus)

print(f'Soma e média dos valores para A(-): Soma = {soma_A_minus:.2f}, Média = {media_A_minus:.2f}')
print(f'Soma e média dos valores para B(-): Soma = {soma_B_minus:.2f}, Média = {media_B_minus:.2f}')
print(f'Soma e média dos valores para C(-): Soma = {soma_C_minus:.2f}, Média = {media_C_minus:.2f}')
print(f'Soma e média dos valores para D(-): Soma = {soma_D_minus:.2f}, Média = {media_D_minus:.2f}')
print(f'Soma e média dos valores para E(-): Soma = {soma_E_minus:.2f}, Média = {media_E_minus:.2f}')
print(f'Soma e média dos valores para F(-): Soma = {soma_F_minus:.2f}, Média = {media_F_minus:.2f}')

# Cálculo do efeito principal
ef_A = media_A_plus - media_A_minus
ef_B = media_B_plus - media_B_minus
ef_C = media_C_plus - media_C_minus
ef_D = media_D_plus - media_D_minus
ef_E = media_E_plus - media_E_minus
ef_F = media_F_plus - media_F_minus

print(f'Efeito Principal para A: {ef_A:.2f}')
print(f'Efeito Principal para B: {ef_B:.2f}')
print(f'Efeito Principal para C: {ef_C:.2f}')
print(f'Efeito Principal para D: {ef_D:.2f}')
print(f'Efeito Principal para E: {ef_E:.2f}')
print(f'Efeito Principal para F: {ef_F:.2f}')

# Valores_variancia para o nível alto (+)
valores_variancia_A_plus = np.array([79.47, 84.58, 91.67, 88.99, 88.88, 98.27, 82.30, 75.11])
valores_variancia_B_plus = np.array([74.09, 80.93, 89.58, 74.24, 88.88, 98.27, 82.30, 75.11])
valores_variancia_C_plus = np.array([88.99, 82.24, 89.58, 74.24, 91.67, 88.99, 82.30, 75.11])
valores_variancia_D_plus = np.array([88.99, 82.24, 74.09, 80.93, 79.47, 84.58, 82.30, 75.11])
valores_variancia_E_plus = np.array([69.40, 82.24, 80.93, 74.24, 84.58, 88.99, 98.27, 75.11])
valores_variancia_F_plus = np.array([69.40, 88.99, 74.09, 74.24, 84.58, 91.67, 88.88, 75.11])

# Cálculos para o nível alto (+)
soma_variancia_A_plus = np.sum(valores_variancia_A_plus)
media_variancia_A_plus = soma_variancia_A_plus / len(valores_variancia_A_plus)

soma_variancia_B_plus = np.sum(valores_variancia_B_plus)
media_variancia_B_plus = soma_variancia_B_plus / len(valores_variancia_B_plus)

soma_variancia_C_plus = np.sum(valores_variancia_C_plus)
media_variancia_C_plus = soma_variancia_C_plus / len(valores_variancia_C_plus)

soma_variancia_D_plus = np.sum(valores_variancia_D_plus)
media_variancia_D_plus = soma_variancia_D_plus / len(valores_variancia_D_plus)

soma_variancia_E_plus = np.sum(valores_variancia_E_plus)
media_variancia_E_plus = soma_variancia_E_plus / len(valores_variancia_E_plus)

soma_variancia_F_plus = np.sum(valores_variancia_F_plus)
media_variancia_F_plus = soma_variancia_F_plus / len(valores_variancia_F_plus)

print(f'Soma e média dos valores de variancia para B(+): Soma = {soma_variancia_A_plus:.2f}, Média = {media_variancia_A_plus:.2f}')
print(f'Soma e média dos valores de variancia para B(+): Soma = {soma_variancia_B_plus:.2f}, Média = {media_variancia_B_plus:.2f}')
print(f'Soma e média dos valores de variancia para C(+): Soma = {soma_variancia_C_plus:.2f}, Média = {media_variancia_C_plus:.2f}')
print(f'Soma e média dos valores de variancia para D(+): Soma = {soma_variancia_D_plus:.2f}, Média = {media_variancia_D_plus:.2f}')
print(f'Soma e média dos valores de variancia para E(+): Soma = {soma_variancia_E_plus:.2f}, Média = {media_variancia_E_plus:.2f}')
print(f'Soma e média dos valores de variancia para F(+): Soma = {soma_variancia_F_plus:.2f}, Média = {media_variancia_F_plus:.2f}')

# Valores_variancia para o nível baixo (-)
valores_variancia_A_minus = np.array([75.39, 69.40, 88.99, 82.24, 74.09, 80.93, 89.58, 74.24])
valores_variancia_B_minus = np.array([75.39, 69.40, 88.99, 82.24, 79.47, 84.58, 91.67, 88.99])
valores_variancia_C_minus = np.array([75.39, 69.40, 74.09, 80.93, 79.47, 84.58, 88.88, 98.27])
valores_variancia_D_minus = np.array([75.39, 69.40, 89.58, 74.24, 91.67, 88.99, 88.88, 98.27])
valores_variancia_E_minus = np.array([75.39, 88.99, 74.09, 89.58, 79.47, 91.67, 88.88, 82.30])
valores_variancia_F_minus = np.array([75.39, 82.24, 80.93, 89.58, 79.47, 88.99, 98.27, 82.30])

# Cálculos para o nível baixo (-)
soma_variancia_A_minus = np.sum(valores_variancia_A_minus)
media_variancia_A_minus = soma_variancia_A_minus / len(valores_variancia_A_minus)

soma_variancia_B_minus = np.sum(valores_variancia_B_minus)
media_variancia_B_minus = soma_variancia_B_minus / len(valores_variancia_B_minus)

soma_variancia_C_minus = np.sum(valores_variancia_C_minus)
media_variancia_C_minus = soma_variancia_C_minus / len(valores_variancia_C_minus)

soma_variancia_D_minus = np.sum(valores_variancia_D_minus)
media_variancia_D_minus = soma_variancia_D_minus / len(valores_variancia_D_minus)

soma_variancia_E_minus = np.sum(valores_variancia_E_minus)
media_variancia_E_minus = soma_variancia_E_minus / len(valores_variancia_E_minus)

soma_variancia_F_minus = np.sum(valores_variancia_F_minus)
media_variancia_F_minus = soma_variancia_F_minus / len(valores_variancia_F_minus)

print(f'Soma e média dos valores de variancia para A(-): Soma = {soma_variancia_A_minus:.2f}, Média = {media_variancia_A_minus:.2f}')
print(f'Soma e média dos valores de variancia para B(-): Soma = {soma_variancia_B_minus:.2f}, Média = {media_variancia_B_minus:.2f}')
print(f'Soma e média dos valores de variancia para C(-): Soma = {soma_variancia_C_minus:.2f}, Média = {media_variancia_C_minus:.2f}')
print(f'Soma e média dos valores de variancia para D(-): Soma = {soma_variancia_D_minus:.2f}, Média = {media_variancia_D_minus:.2f}')
print(f'Soma e média dos valores de variancia para E(-): Soma = {soma_variancia_E_minus:.2f}, Média = {media_variancia_E_minus:.2f}')
print(f'Soma e média dos valores de variancia para F(-): Soma = {soma_variancia_F_minus:.2f}, Média = {media_variancia_F_minus:.2f}')

# Cálculo do efeito principal
ef_variancia_A = media_variancia_A_plus - media_variancia_A_minus
ef_variancia_B = media_variancia_B_plus - media_variancia_B_minus
ef_variancia_C = media_variancia_C_plus - media_variancia_C_minus
ef_variancia_D = media_variancia_D_plus - media_variancia_D_minus
ef_variancia_E = media_variancia_E_plus - media_variancia_E_minus
ef_variancia_F = media_variancia_F_plus - media_variancia_F_minus

print(f'Efeito Principal para A: {ef_variancia_A:.2f}')
print(f'Efeito Principal para B: {ef_variancia_B:.2f}')
print(f'Efeito Principal para C: {ef_variancia_C:.2f}')
print(f'Efeito Principal para D: {ef_variancia_D:.2f}')
print(f'Efeito Principal para E: {ef_variancia_E:.2f}')
print(f'Efeito Principal para F: {ef_variancia_F:.2f}')
