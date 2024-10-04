import permutar as p 

r = p.permutacao(2) * p.permutacao(9) - (2 * 2 * p.permutacao(8)) # Calcula-se todas as possibilidades de Brasil e Portugal como um bloco, lembrando de permutar entre eles
                                                                  # e subtrai-se as possibilidades de EUA e Irã como um bloco, assim como Brasil e Portugal, permutando-se entre eles
print(r, "\n") # 725760                