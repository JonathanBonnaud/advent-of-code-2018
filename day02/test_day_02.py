from day02.day_02 import Day02, Day021


class TestDay02:

    def test_day02_ex1(self):
        input_data = [x.strip() for x in open('input_ex1.txt').readlines()]
        assert Day02(input_data).get_result() == 12

    def test_day02_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()]
        print(Day02(input_data).get_result())


class TestDay021:

    def test_day021_ex1(self):
        input_data = [x.strip() for x in open('input_ex2.txt').readlines()]
        assert Day021(input_data).get_result() == "fgij"

    def test_day021_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()]
        print(Day021(input_data).get_result())  # pbykrmjmizwhxlqnasfgtycdv
