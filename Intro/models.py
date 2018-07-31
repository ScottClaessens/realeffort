from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import time
from otree.models_concrete import PageCompletion


author = 'Scott Claessens - University of Auckland'

doc = """
Real-Effort Task - Intro
"""


class Constants(BaseConstants):
    name_in_url = 'Intro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['vote'] = None


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass