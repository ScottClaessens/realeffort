from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Voting(Page):
    form_model = 'player'
    form_fields = ['vote']

    def vote_choices(self):
        if self.session.config['name'] == 'realeffort7':
            choices = [
                [1, 'Lay off one player at random'],
                [2, 'Take a pay cut']
            ]
        elif self.session.config['name'] == 'realeffort8':
            choices = [
                [1, 'Lay off the weakest player'],
                [2, 'Take a pay cut']
            ]
        random.shuffle(choices)
        return choices

    def vars_for_template(self):
        return {'session': self.session.config['name']}


class VotingWait(WaitPage):
    def after_all_players_arrive(self):
        lay = 0
        cut = 0
        for p in self.group.get_players():
            if p.vote == 1:
                lay += 1
            elif p.vote == 2:
                cut += 1
        for p in self.group.get_players():
            if lay > cut:
                p.participant.vars['vote'] = 'layoff'
            elif cut > lay:
                p.participant.vars['vote'] = 'paycut'
            print('layoff var =', p.participant.vars['vote'])


class VotingResult(Page):
    def vars_for_template(self):
        return {'vote': self.participant.vars['vote']}


page_sequence = [
    Voting,
    VotingWait,
    VotingResult
]
