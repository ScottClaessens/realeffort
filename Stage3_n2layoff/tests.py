from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.player.participant.vars['vote'] != 'paycut' and self.player.id_in_group != 3:
            if self.round_number == 1:
                yield (pages.Intro)
            if self.round_number in [1, 31, 61, 91, 121, 151]:
                yield (pages.Start)
            orders = [[1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1]]
            if self.round_number in range(1, 31) or self.round_number in range(61, 91) or self.round_number in range(
                    121, 151):
                order = orders[0]
            else:
                order = orders[1]
            if self.player.id_in_group == order[0]:
                yield (pages.Task1, {'task': 100})
            else:
                yield (pages.Task2, {'task': 100})
            if self.player.id_in_group == order[0]:
                yield (pages.Task3, {'task2': 100})
            else:
                yield (pages.Task4, {'task2': 100})
            if self.player.id_in_group == order[0]:
                yield (pages.Task5, {'task3': 100})
            else:
                yield (pages.Task6, {'task3': 100})
            if self.round_number in [30, 60, 90, 120, 150, 180]:
                yield (pages.Results)
        else:
            pass
