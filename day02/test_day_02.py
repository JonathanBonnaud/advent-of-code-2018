from day02.day_02 import Day02First, Day02Second


class TestDay02First:

    def test_day02_first_ex1(self):
        input_data = [x.strip() for x in open('input_ex1.txt').readlines()]
        assert Day02First(input_data).get_result() == 12

    def test_day02_first_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()]
        print(Day02First(input_data).get_result())


class TestDay02Second:

    def test_day02_second_ex1(self):
        input_data = [x.strip() for x in open('input_ex2.txt').readlines()]
        assert Day02Second(input_data).get_result() == "fgij"

    def test_day02_second_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()]
        print(Day02Second(input_data).get_result())
