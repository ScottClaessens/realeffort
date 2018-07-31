from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import time
from otree.models_concrete import PageCompletion


author = 'Scott Claessens - University of Auckland'

doc = """
Real-Effort Task - Voting
"""


class Constants(BaseConstants):
    name_in_url = 'Voting'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    vote = models.IntegerField(
        widget=widgets.RadioSelect
    )
