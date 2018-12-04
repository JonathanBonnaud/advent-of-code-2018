from day04.day_04 import Day04First, Day04Second


class TestDay04First:

    def test_order_records(self):
        input_records = [("[1518-11-01 00:05]", "falls asleep"), ("[1518-11-02 00:40]", "falls asleep"),
                         ("[1518-11-01 00:55]", "wakes up"), ("[1518-11-01 23:58]", "Guard #99 begins shift"),
                         ("[1518-11-01 00:00]", "Guard #10 begins shift")]
        expected_records = [("[1518-11-01 00:00]", "Guard #10 begins shift"), ("[1518-11-01 00:05]", "falls asleep"),
                            ("[1518-11-01 00:55]", "wakes up"), ("[1518-11-01 23:58]", "Guard #99 begins shift"),
                            ("[1518-11-02 00:40]", "falls asleep")]
        ordered_records = Day04First.order_records(input_records)
        assert ordered_records == expected_records

    def test_generate_minutes(self):
        print(Day04First.generate_minutes('05', '25'))

    def test_day04_first_ex1(self):
        input_data = [x.strip() for x in open('input_ex1.txt').readlines()]
        assert Day04First(input_data).get_result() == 240

    def test_day04_first_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()]
        print(Day04First(input_data).get_result())


class TestDay04Second:

    def test_day04_second_ex1(self):
        input_data = [x.strip() for x in open('input_ex1.txt').readlines()]
        assert Day04Second(input_data).get_result() == 4455

    def test_day04_second_final(self):
        input_data = [x.strip() for x in open('input.txt').readlines()]
        print(Day04Second(input_data).get_result())
