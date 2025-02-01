def maior_e_menor(L):
    return max(L), min(L)
    
print(*maior_e_menor(list(map(int, input().split()))))