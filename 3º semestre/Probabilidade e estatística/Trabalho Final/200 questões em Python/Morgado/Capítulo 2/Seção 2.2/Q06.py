import permutar as p

res = p.permutacao(10) // p.permutacao(3) # De forma aleatória, há 10! possibilidades de organizar os números no total, 
                                            #mas com a restrição de {2, 3, 5} há 3! possibilidades de organizar essa divisão. Assim dividimos o total de possibilidades pela forma de organizar a restrição.

print(res, "\n")