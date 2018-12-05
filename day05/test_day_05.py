from day05.day_05 import Day05First, Day05Second


class TestDay05First:

    def test_day05_first_ex1(self):
        input_data = "dabAcCaCBAcCcaDA"
        assert Day05First(input_data).get_result() == 10

    def test_day05_first_ex2(self):
        input_data = "dabAcCaCBAcCcaDAA"
        assert Day05First(input_data).get_result() == 11

    def test_day05_first_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()][0]
        print(Day05First(input_data).get_result())


class TestDay05Second:

    def test_day05_second_ex1(self):
        input_data = "dabAcCaCBAcCcaDA"
        assert Day05Second(input_data).get_result() == 4

    def test_day05_second_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()][0]
        print(Day05Second(input_data).get_result())

