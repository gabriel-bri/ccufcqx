import numpy as np

data = {0 : 30, 1 : 25, 2 : 10, 3 : 5, 4 : 2}

n_defeitos = np.array(list(data.keys()))
frequencia = np.array(list(data.values()))

media = np.average(n_defeitos, weights=frequencia)

desvio = np.sqrt(np.average((n_defeitos  - media)**2, weights= frequencia))

print(f"Média: {round(media, 4)}\nDesvio Padrão {round(desvio, 4)}")