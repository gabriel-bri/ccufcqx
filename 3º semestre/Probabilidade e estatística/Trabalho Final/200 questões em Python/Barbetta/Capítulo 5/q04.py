import numpy as np

def media(x, probabilidades):
    return np.sum(x * probabilidades)


def variancia(x, probabilidades, media):
    return np.sum(probabilidades * (x - media)**2)



media_a = media(np.array([0, 1]), np.array([0.5, 0.5]))
variancia_a = variancia(np.array([0, 1]), np.array([0.5, 0.5]), media_a)
print(f'a) {media_a}\n {variancia_a}\n')

media_b = media(np.array([0, 1, 2]), np.array([0.25, 0.5, 0.25]))
variancia_b = variancia(np.array([0, 1, 2]), np.array([0.25, 0.25, 0.25]), media_b)
print(f'b) {media_b}\n {variancia_b}\n')

media_c = media(np.array([0, 1, 2]), np.array([0.36, 0.48, 0.16]))
variancia_c = variancia(np.array([0, 1, 2]), np.array([0.36, 0.48, 0.16]), media_c)
print(f'c) {media_c}\n {variancia_c:.4f}\n')

media_d = media(np.array([0, 1, 2, 3]), np.array([0.216, 0.482, 0.288, 0.064]))
variancia_d = variancia(np.array([0, 1, 2, 3]), np.array([0.216, 0.482, 0.288, 0.064]), media_d)
print(f'd) {media_d:.4f}\n {variancia_d:.4f}\n')
