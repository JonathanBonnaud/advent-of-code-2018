from day08.day_08 import Day08First, Day08Second


class TestDay08First:

    def test_day08_first_ex1(self):
        input_data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        assert Day08First(input_data).get_result() == 138

    def test_day08_first_ex2(self):
        input_data = "1 1 0 1 99 2"
        assert Day08First(input_data).get_result() == 101

    def test_day08_first_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()][0]
        print(Day08First(input_data).get_result())


class TestDay08Second:

    def test_day08_second_ex1(self):
        input_data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        assert Day08Second(input_data).get_result() == 66

    def test_day08_first_ex2(self):
        input_data = "1 1 0 1 99 2"
        assert Day08Second(input_data).get_result() == 0

    def test_day08_second_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()][0]
        print(Day08Second(input_data).get_result())

