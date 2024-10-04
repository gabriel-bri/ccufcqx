import fatorial as f

r = f.fatorial(13) / (f.fatorial(5) * f.fatorial(2)**2)

print(f'a) {r}\n')

va = f.fatorial(12) / (f.fatorial(4) * f.fatorial(2) * f.fatorial(2))

vu = f.fatorial(12) / (f.fatorial(5) * f.fatorial(2))

print(f'b) {va + vu}\n')