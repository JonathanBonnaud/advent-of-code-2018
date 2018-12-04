import re
from collections import defaultdict, Counter
from abstract_day import AbstractDay


class Day04First(AbstractDay):

    @staticmethod
    def order_records(records):
        records.sort(key=lambda x: x[0])
        return records

    @staticmethod
    def split_record(record):
        timestamp = record[0].split()
        action = record[1].split()
        if len(action) == 4:
            action = ''.join(action[1:2])
        else:
            action = ' '.join(action)
        return timestamp, action

    @staticmethod
    def generate_minutes(start, end):
        return [i for i in range(int(start), int(end))]

    def get_result(self):
        input_records = [re.findall('\[(.+)\] (.+)', line)[0] for line in self.input_content]
        ordered_records = self.order_records(input_records)
        res = defaultdict(dict)
        current_guard = ''
        for record in ordered_records:
            timestamp, action = self.split_record(record)
            print(timestamp, action)
            if action.startswith('#'):
                current_guard = action
                res[timestamp[0]][current_guard] = [0, list()]
            elif action == "falls asleep":
                from_minute = timestamp[1].split(':')[1]
            elif action == "wakes up":
                to_minute = timestamp[1].split(':')[1]

                nb = int(to_minute) - int(from_minute)
                if current_guard in res[timestamp[0]]:
                    res[timestamp[0]][current_guard][0] += nb
                    res[timestamp[0]][current_guard][1].extend(self.generate_minutes(from_minute, to_minute))
                else:
                    res[timestamp[0]][current_guard] = [nb, list()]

        res2 = defaultdict(int)
        for date, guards in res.items():
            for guard_id, sleeps in guards.items():
                res2[guard_id] += sleeps[0]
        
        res3 = defaultdict(list)
        for date, guards in res.items():
            for guard_id, sleeps in guards.items():
                res3[guard_id].extend(sleeps[1])

        sleepy_guard = max(res2, key=lambda x: res2[x])
        sleepy_minutes = [(item, count) for item, count in Counter(res3[sleepy_guard]).items() if count > 1]
        sleepy_minute = max(sleepy_minutes, key=lambda x: x[1])

        return int(sleepy_guard[1:]) * sleepy_minute[0]


class Day04Second(Day04First):

    def get_result(self):
        input_records = [re.findall('\[(.+)\] (.+)', line)[0] for line in self.input_content]
        ordered_records = self.order_records(input_records)
        res = defaultdict(dict)
        current_guard = ''
        for record in ordered_records:
            timestamp, action = self.split_record(record)
            print(timestamp, action)
            if action.startswith('#'):
                current_guard = action
                res[timestamp[0]][current_guard] = [0, list()]
            elif action == "falls asleep":
                from_minute = timestamp[1].split(':')[1]
            elif action == "wakes up":
                to_minute = timestamp[1].split(':')[1]

                nb = int(to_minute) - int(from_minute)
                if current_guard in res[timestamp[0]]:
                    res[timestamp[0]][current_guard][0] += nb
                    res[timestamp[0]][current_guard][1].extend(self.generate_minutes(from_minute, to_minute))
                else:
                    res[timestamp[0]][current_guard] = [nb, self.generate_minutes(from_minute, to_minute)]

        res3 = defaultdict(list)
        for date, guards in res.items():
            for guard_id, sleeps in guards.items():
                print(guard_id, sleeps)
                res3[guard_id].extend(sleeps[1])

        sleepy_minutes = [(guard_id, item, count) for guard_id in res3 for item, count in Counter(res3[guard_id]).items() if count > 1]
        sleepy_minute = max(sleepy_minutes, key=lambda x: x[2])

        return int(sleepy_minute[0][1:]) * int(sleepy_minute[1])
