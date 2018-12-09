from collections import defaultdict, deque
from abstract_day import AbstractDay


class Day09First(AbstractDay):

    def get_result(self):
        nb_players, last_marble = self.input_content
        players = defaultdict(int)

        the_circle = [0]
        current_marble_index = 0
        for marble in range(1, last_marble+1):
            the_circle_len = len(the_circle)
            if marble % 23 == 0:
                index = (current_marble_index - 7) % the_circle_len
                players[marble % nb_players] += marble + the_circle.pop(index)
            else:
                index = (current_marble_index + 1) % the_circle_len + 1
                the_circle.insert(index, marble)
            current_marble_index = index
        return max(players.values())


class Day09Second(Day09First):
    """
    Optimised version of Day09First using deque list
    """
    def get_result(self):
        nb_players, last_marble = self.input_content
        players = defaultdict(int)

        the_circle = deque([0])
        for marble in range(1, last_marble + 1):
            if marble % 23 == 0:
                the_circle.rotate(7)
                players[marble % nb_players] += marble + the_circle.pop()
                the_circle.rotate(-1)
            else:
                the_circle.rotate(-1)
                the_circle.append(marble)
        return max(players.values())

