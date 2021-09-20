from math import sqrt
import numpy as np


def euclidian_distance(pos, dest):
    return sqrt((dest[0] - pos[0]) ** 2 + (dest[1] - pos[1]) ** 2)


def manhattan_distance(pos, dest):
    return np.sum(np.abs(np.array(pos) - np.array(dest)))
