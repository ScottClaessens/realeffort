from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.player.participant.vars['vote'] != 'paycut':
            yield (pages.Layoff)
            if self.player.id_in_group == 3:
                yield (pages.Layoff2)
