import permutar as p

print("Item a)\n")

res = 81 # Partindo se de que cada número tem a possibilidade de ser acompanhado por 4! algarismos, sabe-se que existe 24 possibilidades para cada número isoladamente
        # Assim números começados com 1, 2, ou 4 somam-se 72 posições. Começando a próxima rodada com os algarismos 61 e 3! para as demais possibilidades, temos 6 possibilidades
        # Assim, sabe-se que 72 + 6 = 78 posições. Contando a partir de números começados com 62, fica fácil ver que 62417 fica na posição 81

print(res, "\n")

print("Item b)\n")

res = 46721 # Sabendo que 41 e 3! chega-se há 54 posições. Basta verificar os números iniciados por 42 e 46.

print(res, "\n")

print("Item c)\n")

res = 1 # Dividindo 200 posições por 5 digitos, temos 40 posições para cada número. Assim, usando a mesma lógica dos itens passados
        # Vemos que o número na posição 40 é 26471, e o seu último número é 1.

print(res, "\n")

print("Item d)\n")

dezenaMilhar = 24 * (10000 + 20000 + 40000 + 60000 + 70000) # 24 está em evidência, já que cada algarismo na dezena de milhar tem 24 possibilidades
milhar = 24 * (1000 + 2000 + 4000 + 6000 + 7000) # 24 possibilidades para cada algarismo na casa do milhar
centena = 24 * (100 + 200 + 400 + 600 + 700) # 24 possibilidades para cada algarismo na casa da centena
dezena = 24 * (10 + 20 + 40 + 60 + 70) # 24 possibilidades para cada algarismo na casa da dezena
unidade = 24 * (1 + 2 + 4 + 6 + 7) # 24 possibilidades para cada algarismo na casa da unidade
res = dezenaMilhar + milhar + centena + dezena + unidade

print(res, "\n")