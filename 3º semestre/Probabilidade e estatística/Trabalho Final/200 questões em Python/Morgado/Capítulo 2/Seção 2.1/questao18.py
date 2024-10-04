# Contando o número de zeros nas unidades
zeros_units = 222222 // 10

# Contando o número de zeros nas dezenas
zeros_tens = 222222 // 100 * 10

# Contando o número de zeros nas centenas
zeros_hundreds = 222222 // 1000 * 100

# Contando o número de zeros nos milhares
zeros_thousands = 222222 // 10000 * 1000

# Contando o número de zeros nas dezenas de milhar
zeros_ten_thousands = 222222 // 100000 * 10000

# Totalizando o número de zeros
total_zeros = zeros_units + zeros_tens + zeros_hundreds + zeros_thousands + zeros_ten_thousands

print("O algarismo zero é escrito", total_zeros, "vezes.")
