import permSimples as p
import fatorial as f

# 
a = p.permSimples(20, 10) / f.fatorial(2)
print(f'a) {a} \n')

b = (p.permSimples(20, 5) * p.permSimples(15, 5) * p.permSimples(10, 5) * p.permSimples(5, 5)) / f.fatorial(4)
print(f'b) {b}\n')

c = (p.permSimples(20, 12) * p.permSimples(8, 8)) 

print(f'c) {c}\n')

d = (p.permSimples(20, 6) * p.permSimples(14, 6) * p.permSimples(8, 6) * p.permSimples(2, 2)) / (f.fatorial(3))

print(f'd) {d}\n')