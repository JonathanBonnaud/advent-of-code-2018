from day06.day_06 import Day06First, Day06Second


class TestDay06First:

    def test_day06_first_ex1(self):
        input_data = [x.strip() for x in open('input_ex1.txt').readlines()]
        assert Day06First(input_data).get_result() == 17

    def test_day06_first_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()]
        print(Day06First(input_data).get_result())


class TestDay06Second:

    def test_day06_second_ex1(self):
        input_data = [x.strip() for x in open('input_ex1.txt').readlines()]
        assert Day06Second(input_data).get_result() == 0

    def test_day06_second_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()]
        print(Day06Second(input_data).get_result())

