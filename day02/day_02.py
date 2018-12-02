import itertools
from collections import Counter
from Levenshtein import editops
from abstract_day import AbstractDay


class Day02(AbstractDay):

    def get_result(self):
        count_2, count_3 = 0, 0
        for box_id in self.input_content:
            occurrences = Counter(box_id)
            count_2 += 1 if next((nb for nb in occurrences.values() if nb == 2), None) else 0
            count_3 += 1 if next((nb for nb in occurrences.values() if nb == 3), None) else 0
        return count_2 * count_3


class Day021(AbstractDay):

    def get_result(self):
        min_pair = min(itertools.combinations(self.input_content, 2), key=lambda pair: len(editops(*pair)))
        remove_pos = [pos[1] for pos in editops(*min_pair)]
        final_str = ''.join([char for i, char in enumerate(min_pair[0]) if i not in remove_pos])
        return final_str
