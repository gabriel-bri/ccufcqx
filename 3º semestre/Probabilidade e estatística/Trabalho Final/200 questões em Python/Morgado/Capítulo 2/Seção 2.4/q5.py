def contar_zragonos(n):
    if n < 3:
        return 0
    else:
        fatorial = 1
        for i in range(1, n):
            fatorial *= i
        
        # Retorna (n - 1)! dividido por 2
        return fatorial // 2

n = int(input("Digite o número de pontos no círculo: "))
num_zragonos = contar_zragonos(n)
print("Número de zr-ágonos:", num_zragonos)
