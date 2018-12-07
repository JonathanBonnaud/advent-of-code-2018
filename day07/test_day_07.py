from day07.day_07 import Day07First, Day07Second


class TestDay07First:

    def test_day07_first_ex1(self):
        input_data = [x.strip() for x in open('input_ex1.txt').readlines()]
        assert Day07First(input_data).get_result() == "CABDFE"

    def test_day07_first_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()]
        print(Day07First(input_data).get_result())


class TestDay07Second:

    def test_day07_second_ex1(self):
        input_data = [x.strip() for x in open('input_ex1.txt').readlines()]
        assert Day07Second(input_data).get_result(2, 0) == 15

    def test_day07_second_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()]
        print(Day07Second(input_data).get_result(5, 60))

