import math

ways_to_arrange_AC = math.comb(12, 5)
ways_to_arrange_B = math.comb(13, 6)
total_arrangements = ways_to_arrange_AC * ways_to_arrange_B

print("O número total de arranjos possíveis é:", total_arrangements)
