from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Scott Claessens - University of Auckland'

doc = """
Real-Effort Task - Stage 2
"""


class Constants(BaseConstants):
    name_in_url = 'Stage2'
    players_per_group = 3
    num_rounds = 180


class Subsession(BaseSubsession):
    def creating_session(self):
        self.session.vars['numbers2'] = []
        for n in range(3, 7):
            random.seed(n)
            self.session.vars['numbers2'].append(random.sample(list(range(10, 100)) * 3, 180))
        for p in self.get_players():
            p.participant.vars['stage2_attempted_individual'] = 0
            p.participant.vars['stage2_correct_individual'] = 0
        for g in self.get_groups():
            p1 = g.get_player_by_id(1)
            p1.participant.vars['stage2_attempted_cycles'] = 0
            p1.participant.vars['stage2_correct_cycles'] = 0
            p1.participant.vars['stage2_currentcyclecorrect?'] = False


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    task = models.IntegerField(
        min=20,
        max=396
    )

    attempted_individual = models.IntegerField()
    correct_individual = models.IntegerField()
    attempted_cycles = models.IntegerField()
    correct_cycles = models.IntegerField()
