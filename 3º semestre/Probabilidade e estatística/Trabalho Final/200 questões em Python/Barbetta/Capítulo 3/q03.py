import numpy as np

data = [7, 8, 6, 10, 5, 9, 4, 12, 7, 8]

media = np.mean(data)

desv = np.std(data, ddof = 1)

print(f"a) {media}\nb) {round(desv, 2)}")