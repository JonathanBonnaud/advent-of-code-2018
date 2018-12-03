from abstract_day import AbstractDay


class Day01First(AbstractDay):

    def get_result(self):
        return sum(self.input_content)


class Day01Second(AbstractDay):

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


class Day01SecondBis(AbstractDay):

    def __init__(self, input_content):
        super().__init__(input_content)
        self.tot = 0
        self.seen = {0}

    def cond(self, x):
        self.tot += x
        if self.tot in self.seen:
            return True
        else:
            self.seen.add(self.tot)
            return False

    def get_result(self):
        res = next((self.tot for x in self.input_content if self.cond(x)), None)
        return res if res is not None else self.get_result()
