import math

def contar_inteiros_nao_perfeitos(limite):
    #quadrados (sqrt para calcular raiz)
    max_square_root = int(math.sqrt(limite))
    quadrados_perfeitos = max_square_root
    
    #cubos perfeitos
    max_cube_root = int(limite ** (1/3))
    cubos_perfeitos = max_cube_root
    
    # Contar números que são ambos (sextos poderes)
    max_sixth_root = int(limite ** (1/6))
    sextos_poderes = max_sixth_root
    
    #princípio da inclusão-exclusão
    inteiros_totais = limite
    inteiros_comum = quadrados_perfeitos + cubos_perfeitos - sextos_poderes
    
    return inteiros_totais - inteiros_comum

limite = 1000000
resultado = contar_inteiros_nao_perfeitos(limite)
print(f"Número de inteiros entre 1 e {limite} que não são nem quadrados perfeitos nem cubos perfeitos: {resultado}")
