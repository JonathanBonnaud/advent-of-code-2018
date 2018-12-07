import re
import string
from collections import defaultdict

from abstract_day import AbstractDay


class Day07First(AbstractDay):

    @staticmethod
    def preprocessing(input_data):
        regex = re.compile("Step (.) must be finished before step (.) can begin.")
        steps = defaultdict(set)
        all_values = set()
        for instruction in input_data:
            first, second = regex.search(instruction).groups()
            steps[second].add(first)
            all_values.add(first)
            all_values.add(second)
        end = next(iter(all_values - {val for list_val in steps.values() for val in list_val}))
        starts = list(all_values - {val for list_val in steps.keys() for val in list_val})
        return steps, all_values, starts, end

    def get_result(self, *args):
        steps, _, starts, end = self.preprocessing(self.input_content)

        steps_order = list()
        stack = sorted(starts)
        current_step = stack.pop(0)
        while current_step != end:
            steps_order.append(current_step)
            now_ready = {step for step, ready_step in steps.items() if current_step in ready_step and set(steps_order) >= ready_step}
            stack.extend(now_ready)
            stack.sort()
            current_step = stack.pop(0)
        return ''.join(steps_order + [end])


class Day07Second(Day07First):

    def get_result(self, nb_workers, default_step_duration):
        steps, alphabet, starts, end = self.preprocessing(self.input_content)
        steps_durations = {
            letter: default_step_duration + string.ascii_uppercase.index(letter) + 1 for letter in alphabet
        }

        time_count = 0
        workers = set()
        steps_done = list()
        stack = sorted(starts)

        for step in stack:
            if step not in workers and len(workers) < nb_workers:
                workers.add(step)

        while stack:
            time_count += 1
            for current_step in stack:
                if current_step not in workers and len(workers) < nb_workers:
                    workers.add(current_step)
            steps_durations.update({step: duration-1 for step, duration in steps_durations.items() if step in workers})

            for current_step in stack:
                if steps_durations[current_step] == 0:
                    steps_done.append(current_step)
                    workers.remove(current_step)
                    now_ready = {step for step, ready_step in steps.items() if
                                 current_step in ready_step and set(steps_done) >= ready_step}
                    stack.remove(current_step)
                    stack.extend(now_ready)
                    stack.sort()

        return time_count

