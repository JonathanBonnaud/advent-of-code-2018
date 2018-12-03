from day03.day_03 import Day03First, Day03Second, Day03FirstBest


class TestDay03First:

    def test_day03_first_ex1(self):
        input_data = [x.strip() for x in open('input_ex1.txt').readlines()]
        assert Day03FirstBest(input_data).get_result() == 4

    def test_day03_first_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()]
        print(Day03FirstBest(input_data).get_result())


class TestDay03Second:

    def test_day03_second_ex1(self):
        input_data = [x.strip() for x in open('input_ex1.txt').readlines()]
        assert Day03Second(input_data).get_result() == {3}

    def test_day03_second_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()]
        print(Day03Second(input_data).get_result())
