def criar_domino():
    dominos = []
    for i in range(7):
        for j in range(i, 7):
            dominos.append((i, j))
    return dominos

dominos = criar_domino()
print("Peças de dominó comuns:", dominos)
print("Número total de peças:", len(dominos))
