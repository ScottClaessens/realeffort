from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Scott Claessens - University of Auckland'

doc = """
Real-Effort Task - Stage 1
"""


class Constants(BaseConstants):
    name_in_url = 'Stage1'
    players_per_group = None
    num_rounds = 180


class Subsession(BaseSubsession):
    def creating_session(self):
        random.seed(1)
        num1 = random.sample(list(range(10, 100)) * 3, 180)
        random.seed(2)
        num2 = random.sample(list(range(10, 100)) * 3, 180)
        self.session.vars['numbers1'] = [num1, num2]
        for p in self.get_players():
            p.participant.vars['stage1_attempted'] = 0
            p.participant.vars['stage1_correct'] = 0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    task = models.IntegerField(
        min=20,
        max=198
    )

    attempted = models.IntegerField()
    correct = models.IntegerField()
