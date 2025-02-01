def remove_elemento(L, p):
    return list(filter(lambda x: x != p, L))

print(*remove_elemento(list(map(int, input().split())), int(input())))