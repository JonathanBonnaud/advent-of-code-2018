import numpy as np
from scipy.spatial.distance import euclidean
from abstract_day import AbstractDay


class Day06First(AbstractDay):

    def get_result(self):
        grid = np.zeros((300, 300))

        x1 = np.array((2, 2))
        x2 = np.array((1, 6))

        out = euclidean(x1, x2)
        print(out)
        return 0


class Day06Second(AbstractDay):

    def get_result(self):
        return 0
