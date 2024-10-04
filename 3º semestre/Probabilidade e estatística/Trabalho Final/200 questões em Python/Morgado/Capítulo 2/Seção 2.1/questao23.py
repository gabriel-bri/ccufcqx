# Número total de números de cinco dígitos
total_numeros = 10 ** 5

# Número total de cartões do tipo (III) que exibem dois números diferentes quando virados de cabeça para baixo
cartoes_tipo_III = (5 ** 5) - 75

# Número de cartões que podem ser economizados (cada cartão do tipo III representa dois números diferentes)
cartoes_economizados = cartoes_tipo_III // 2

# Número mínimo de cartões necessário para representar todos os números de cinco dígitos
numero_minimo_cartoes = total_numeros - cartoes_economizados

print("O número mínimo de cartões necessário é:", numero_minimo_cartoes)
