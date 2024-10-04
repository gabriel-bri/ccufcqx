total_colecoes = 0

# Caso 1: Primeira carta é um Rei de Copas
# Uma possibilidade para o Rei de Copas
# Três possibilidades para escolher um Rei após a primeira extração
# 46 possibilidades para escolher uma carta que não seja uma Dama
total_colecoes += 1 * 3 * 46

# Caso 2: Primeira carta de copas não é um Rei de Copas
# 11 possibilidades para escolher uma carta que não seja um Rei de Copas
# Quatro possibilidades para escolher um Rei após a primeira extração
# 46 possibilidades para escolher uma carta que não seja uma Dama
total_colecoes += (52 - 4 - 1) // 4 * 4 * 46 

# Caso 3: Primeira carta é uma Dama de Copas
# Uma possibilidade para a Dama de Copas
# Quatro possibilidades para escolher um Rei após a primeira extração
# 47 possibilidades para escolher uma carta que não seja uma Dama
total_colecoes += 1 * 4 * 47

print("Total de coleções que atendem às condições especificadas:", total_colecoes)
