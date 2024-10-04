import math

def permutations(n, k):
    return math.factorial(n) // math.factorial(n - k)

# Número total de passageiros
total_passengers = 10
front_facing = 4
back_facing = 3

no_preference = total_passengers - front_facing - back_facing

ways_front_facing = permutations(5, front_facing)

ways_back_facing = permutations(5, back_facing)

total_ways = ways_front_facing * ways_back_facing * math.factorial(no_preference)

print("Número total de maneiras:", total_ways)
