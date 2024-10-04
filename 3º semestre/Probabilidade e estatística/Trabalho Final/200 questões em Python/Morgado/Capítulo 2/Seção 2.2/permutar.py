def permutacao(n):
  if(n == 0):
    return 1
  else:
    return n * permutacao(n - 1)
