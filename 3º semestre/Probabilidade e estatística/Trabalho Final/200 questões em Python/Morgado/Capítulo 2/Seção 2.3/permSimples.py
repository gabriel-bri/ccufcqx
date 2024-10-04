import fatorial as f

def permSimples(m, p):
    return ((f.fatorial(m)) /( f.fatorial(p) * f.fatorial(m - p)) )
