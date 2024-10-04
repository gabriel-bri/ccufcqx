import permSimples as p
import fatorial as f
# Modos de se escolher cada casal >> Organizaçao dos espaços vazios >> Organizaçao dos seis casais nos seis lugares restantes

r = (2**6) * p.permSimples(14, 8) *  f.fatorial(6)

print(r)