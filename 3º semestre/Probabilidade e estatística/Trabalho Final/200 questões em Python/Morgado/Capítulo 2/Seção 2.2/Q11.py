import permutar as p

r = p.permutacao(6) // 24 # Há 4 possibilidades de escolhas para a face ficar de frente, já que a sua parte oposta é indiferenciável
                        # Como há 6 faces ao todo no cubo, temos que 6*4 = 24. Já que há 6! possibilidades de confecção do cubo em 6 grupos de 4 faces

print(r, "\n")