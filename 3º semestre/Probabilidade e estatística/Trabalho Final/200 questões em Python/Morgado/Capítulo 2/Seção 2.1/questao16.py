def count_routes(n):
    # Inicialmente, há uma única rota (não há movimentos)
    routes = 1
    # Para cada movimento adicional
    for i in range(n):
        
        routes *= 2
    
    return routes

n = 11

total_routes = count_routes(n)

print("Número total de rotas:", total_routes)
