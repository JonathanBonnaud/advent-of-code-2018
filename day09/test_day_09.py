from day09.day_09 import Day09First, Day09Second


class TestDay09First:

    def test_day09_first_ex1(self):
        input_data = (9, 25)
        assert Day09First(input_data).get_result() == 32

    def test_day09_first_ex2(self):
        input_data = (10, 1618)
        assert Day09First(input_data).get_result() == 8317

    def test_day09_first_ex3(self):
        input_data = (13, 7999)
        assert Day09First(input_data).get_result() == 146373

    def test_day09_first_ex4(self):
        input_data = (17, 1104)
        assert Day09First(input_data).get_result() == 2764

    def test_day09_first_ex5(self):
        input_data = (21, 6111)
        assert Day09First(input_data).get_result() == 54718

    def test_day09_first_ex6(self):
        input_data = (30, 5807)
        assert Day09First(input_data).get_result() == 37305

    def test_day09_first_final(self):
        input_data = (441, 71032)
        print(Day09First(input_data).get_result())


class TestDay09Second:

    def test_day09_second_final(self):
        input_data = (441, 7103200)
        print(Day09Second(input_data).get_result())

