from day01.day_01 import Day01First, Day01Second


class TestDay01First:

    def test_day01_first_ex1(self):
        assert Day01First([+1, -2, +3, +1]).get_result() == 3

    def test_day01_first_final(self):
        input_data = [int(x) for x in open('input.txt').readlines()]
        print(Day01First(input_data).get_result())


class TestDay01Second:

    def test_day01_second_ex1(self):
        l = [+1, -2, +3, +1]
        assert Day01Second(l).get_result() == 2

    def test_day01_second_ex2(self):
        l = [+1, -1]
        assert Day01Second(l).get_result() == 0

    def test_day01_second_ex3(self):
        l = [+3, +3, +4, -2, -4]
        assert Day01Second(l).get_result() == 10

    def test_day01_second_ex4(self):
        l = [-6, +3, +8, +5, -6]
        assert Day01Second(l).get_result() == 5

    def test_day01_second_ex5(self):
        l = [+7, +7, -2, -7, -4]
        assert Day01Second(l).get_result() == 14

    def test_day01_second_final(self):
        input_data = [int(x) for x in open('input.txt').readlines()]
        print(Day01Second(input_data).get_result())
