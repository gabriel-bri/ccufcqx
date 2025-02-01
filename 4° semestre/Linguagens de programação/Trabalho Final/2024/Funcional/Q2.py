def maior_e_posicao(L):
    return max(L), L.index(max(L))

print(*maior_e_posicao(list(map(int, input().split()))))