import os

base_script = """from abstract_day import AbstractDay


class Day{day}First(AbstractDay):

    def get_result(self):
        return 0


class Day{day}Second(AbstractDay):

    def get_result(self):
        return 0

"""

base_test = """from day{day}.day_{day} import Day{day}First, Day{day}Second


class TestDay{day}First:

    def test_day{day}_first_ex1(self):
        input_data = [x.strip() for x in open('input_ex1.txt').readlines()]
        assert Day{day}First(input_data).get_result() == 0

    def test_day{day}_first_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()]
        print(Day{day}First(input_data).get_result())


class TestDay{day}Second:

    def test_day{day}_second_ex1(self):
        input_data = [x.strip() for x in open('input_ex1.txt').readlines()]
        assert Day{day}Second(input_data).get_result() == 0

    def test_day{day}_second_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()]
        print(Day{day}Second(input_data).get_result())

"""

if __name__ == '__main__':
    import argparse

    def arguments():
        parser = argparse.ArgumentParser(description='Script desc')
        parser.add_argument(
            'day', type=int, help='Day to create')
        args = parser.parse_args()
        return args

    args = arguments()

    day_number = '{:0>2}'.format(args.day)
    dir_name = f'day{day_number}/'

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    file_name = f'day_{day_number}'
    with open(dir_name + file_name + '.py', 'w') as f:
        f.write(base_script.format(day=day_number))

    with open(dir_name + 'test_' + file_name + '.py', 'w') as f:
        f.write(base_test.format(day=day_number))

    with open(dir_name + 'input_ex1.txt', 'w') as f:
        f.write('')
