# Definir os números totais e os contadores
total_numbers = 200
div_by_5 = total_numbers // 5
div_by_7 = total_numbers // 7
div_by_35 = total_numbers // 35

# Calcular a quantidade de números divisíveis por 5 ou 7
count_div_by_5_or_7 = div_by_5 + div_by_7 - div_by_35

# Calcular a probabilidade
probability = count_div_by_5_or_7 / total_numbers

print(f"A probabilidade de que um número escolhido aleatoriamente entre 1 e 200 seja divisível por 5 ou por 7 é: {probability:.4f}")
