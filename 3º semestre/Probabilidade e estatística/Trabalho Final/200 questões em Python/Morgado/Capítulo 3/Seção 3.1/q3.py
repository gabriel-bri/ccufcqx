import itertools

combinations = list(itertools.product(range(1, 7), repeat=3))
valid_combinations = [combo for combo in combinations if sum(combo) == 12]
result = len(valid_combinations)
print(result)
