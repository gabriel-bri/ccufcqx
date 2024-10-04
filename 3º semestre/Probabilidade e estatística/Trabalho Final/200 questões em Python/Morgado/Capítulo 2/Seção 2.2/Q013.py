import permutar as p

res = p.permutacao(12) // (p.permutacao(2) * p.permutacao(2) * p.permutacao(2) * p.permutacao(2) * p.permutacao(2) * p.permutacao(2) * p.permutacao(6)  )
# Mesma lógica do item d) da Q07_nex.py, só que são 12 times e como cada jogo precisa de dois times, temos 6! possibilidades de combinações de partidas, multiplica-se isso pela permutação da disposição dos times em cada jogo
print(res, "\n")