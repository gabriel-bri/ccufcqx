import permSimples as p 
import fatorial as f 

convidados =( ( p.permSimples(6, 2) *  p.permSimples(4, 2) * 1 )/ f.fatorial(3) ) * 2

r = f.fatorial(7) * convidados

print(r)

