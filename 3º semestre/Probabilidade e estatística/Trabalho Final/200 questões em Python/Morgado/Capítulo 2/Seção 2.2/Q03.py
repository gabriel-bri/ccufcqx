import permutar as p

res = p.permutacao(7) - 2 * p.permutacao(6) # Calcula-se primeiro todas as posições possíveis, 
                                            # Subtrai-se os casos em que as pessoas A e B estão juntas,
                                            # Como A pode vir na frente de B e vice-versa, multiplica-se por 2!, para indicar que permutam entre si
print(res, "\n")