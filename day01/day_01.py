from abstract_day import AbstractDay


class Day01(AbstractDay):

    def get_result(self):
        return sum(self.input_content)


class Day012(AbstractDay):

    def get_result(self):
        res = 0
        seen = set()
        i = 0
        while res not in seen:
            seen.add(res)
            if i == len(self.input_content):
                i = 0
            res += self.input_content[i]
            i += 1
        return res
