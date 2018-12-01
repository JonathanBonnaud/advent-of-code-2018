from day01.day_01 import Day01, Day012


class TestDay01:

    def test_day01_ex1(self):
        assert Day01([+1, -2, +3, +1]).get_result() == 3

    def test_day01_final(self):
        input_data = [int(x) for x in open('input.txt').readlines()]
        print(Day01(input_data).get_result())


class TestDay012:

    def test_day012_ex1(self):
        l = [+1, -2, +3, +1]
        assert Day012(l).get_result() == 2

    def test_day012_ex2(self):
        l = [+1, -1]
        assert Day012(l).get_result() == 0

    def test_day012_ex3(self):
        l = [+3, +3, +4, -2, -4]
        assert Day012(l).get_result() == 10

    def test_day012_ex4(self):
        l = [-6, +3, +8, +5, -6]
        assert Day012(l).get_result() == 5

    def test_day012_ex5(self):
        l = [+7, +7, -2, -7, -4]
        assert Day012(l).get_result() == 14

    def test_day01_final(self):
        input_data = [int(x) for x in open('input.txt').readlines()]
        print(Day012(input_data).get_result())
