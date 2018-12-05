import re
import numpy as np
from abstract_day import AbstractDay


class Day03First(AbstractDay):

    @staticmethod
    def check_elf_claims(matrix, claims):
        for elf_claim in claims:
            parts = re.findall('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', elf_claim)
            parts = list(map(int, list(parts[0])))
            for i in range(parts[2] + parts[4]):
                if len(matrix) <= i:
                    matrix.append([[set(), 0] for _ in range(parts[1] + parts[3])])
                if i in range(parts[2], parts[2] + parts[4] + 1):
                    for j in range(parts[1] + parts[3]):
                        if len(matrix[i]) <= j:
                            matrix[i].append([set(), 0])
                        if j in range(parts[1], parts[1] + parts[3] + 1):
                            matrix[i][j][0].add(parts[0])
                            matrix[i][j][1] += 1

    def get_result(self):
        matrix = list()
        self.check_elf_claims(matrix, self.input_content)
        return sum([1 for line in matrix for cell in line if cell[1] > 1])


class Day03Second(Day03First):

    def get_result(self):
        matrix = list()
        self.check_elf_claims(matrix, self.input_content)
        overlaps = set().union(*[set(cell[0]) for line in matrix for cell in line if cell[1] > 1])
        return set().union(*[cell[0] for line in matrix for cell in line if cell[1] == 1 and not (cell[0] & overlaps)])


class Day03FirstBest(AbstractDay):

    def get_result(self):
        matrix = np.zeros((1000, 1000))
        regex = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
        for claim in self.input_content:
            parts = list(map(int, regex.search(claim).groups()))

            i, y_offset, x_offset, y_limit, x_limit = parts
            matrix[x_offset:x_offset+x_limit, y_offset:y_offset+y_limit] += 1
        return len(matrix[np.where(matrix > 1.0)])
