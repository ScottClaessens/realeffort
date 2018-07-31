from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from random import *


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Voting, {'vote': 2})
        yield (pages.VotingResult)
