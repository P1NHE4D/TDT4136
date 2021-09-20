from math import sqrt


def euclidian_distance(pos, dest):
    return sqrt((dest[0] - pos[0]) ** 2 + (dest[1] - pos[1]) ** 2)
