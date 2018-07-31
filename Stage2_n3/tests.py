from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Intro)
        if self.round_number in [1, 31, 61, 91, 121, 151]:
            yield (pages.Start)
        orders = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
        if self.round_number in range(1, 31) or self.round_number in range(91, 121):
            order = orders[0]
        elif self.round_number in range(31, 61) or self.round_number in range(121, 151):
            order = orders[1]
        else:
            order = orders[2]
        if self.player.id_in_group == order[0]:
            yield (pages.Task1, {'task': 100})
        elif self.player.id_in_group == order[1]:
            yield (pages.Task2, {'task': 100})
        else:
            yield (pages.Task3, {'task': 100})
        if self.round_number in [30, 60, 90, 120, 150, 180]:
            yield (pages.Results)
