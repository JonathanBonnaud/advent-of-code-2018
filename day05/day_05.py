import string
import re

from abstract_day import AbstractDay


class Day05First(AbstractDay):
    data = {c: c.upper() for c in string.ascii_lowercase}
    data.update({c: c.lower() for c in string.ascii_uppercase})

    def get_result(self):
        polymer = self.input_content
        i = 0
        while i+1 < len(polymer):
            if self.data[polymer[i]] == polymer[i+1]:
                polymer = polymer[:i] + polymer[i+2:]
                i -= 1 if i else 0
            else:
                i += 1
        return len(polymer)


class Day05Second(AbstractDay):

    @staticmethod
    def remove_all(polymer, letter):
        up_low_letter = letter.lower() + letter.upper()
        clean_polymer = re.sub(f'[{up_low_letter}]', '', polymer)
        return clean_polymer

    def get_result(self):
        polymer = self.input_content
        polymer_lengths = [Day05First(self.remove_all(polymer, letter)).get_result() for letter in string.ascii_lowercase]
        return min(polymer_lengths)

