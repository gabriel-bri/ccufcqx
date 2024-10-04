import permutar as p


print("Item a)\n ")

res = 4 * 4 *   p.permutacao(6) # Quatro possibilidades para ser consoante, quatro possibilidades para ser vogal e as demais letras

print(res, "\n")

print("Item b)\n ")

res =  p.permutacao(6) #Como {C, A, P} é um bloco só, podemos tratá-lo como uma única letra, assim temos 6 letras para organizar 

print(res, "\n")

print("Item c)\n ")

res =  p.permutacao(3) * p.permutacao(6) # Formas de organizar {C, A, P} e formas de organizar as demais letras

print(res, "\n")

print("Item d)\n ")

res =  p.permutacao(4) * p.permutacao(4) # Cada consoante tem 4 possibilidades e cada vogal tem 4 possibilidades
res = res * 2 # Multiplica-se para representar que podem ser vogais ou consoantes no começo

print(res, "\n")

print("Item e)\n ")

res = 1 * 1 * p.permutacao(6) # Como C e A são fixos, temos apenas 6 letras para organizar

print(res, "\n")

print("Item f)\n ")

res =  p.permutacao(7) + p.permutacao(7) - p.permutacao(6) #Calcula-se primeiramente os casos que C e A são definidos, sobrando 7 letras para organizar em cada caso,
                                                            #subtrai-se isso pelo número de casos com C na primeira posição e A na segunda posição 

print(res, "\n")


print("Item g)\n ")

res =  p.permutacao(7) + p.permutacao(7) + p.permutacao(7) - p.permutacao(6) - p.permutacao(6) - p.permutacao(6) + p.permutacao(5) 
                                                        #Pelo princípio da inclusão exclusão, primeiro soma-se os casos que C, A e P são definidos, sobrando 7 letras para organizar em cada caso,
                                                        #subtrai-se isso pelo número de casos com C intersectando A, C intersectando P e A intersectando P, 
                                                        # e soma-se o número de casos com C intersectando A intersectando P 

print(res, "\n")
