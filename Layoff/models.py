from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import time
from otree.models_concrete import PageCompletion


author = 'Scott Claessens - University of Auckland'

doc = """
Real-Effort Task - Layoff
"""


class Constants(BaseConstants):
    name_in_url = 'Layoff'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def layoff(self):
        if self.round_number == 1:
            print('layoff happening...')
            if self.session.config['layoff'] == 'random':
                players = self.get_players()
                # shuffle group randomly, player 3 laid off
                random.shuffle(players)
                self.set_players(players)
                print('layoff = random, SHUFFLE')
            elif self.session.config['layoff'] == 'weak':
                player_tuples = [
                    (self.get_player_by_id(1),
                     self.get_player_by_id(1).participant.vars['stage2_total_mistakes_individual'],
                     self.get_player_by_id(1).participant.vars['stage2_idletime']),
                    (self.get_player_by_id(2),
                     self.get_player_by_id(2).participant.vars['stage2_total_mistakes_individual'],
                     self.get_player_by_id(2).participant.vars['stage2_idletime']),
                    (self.get_player_by_id(3),
                     self.get_player_by_id(3).participant.vars['stage2_total_mistakes_individual'],
                     self.get_player_by_id(3).participant.vars['stage2_idletime']),
                ]
                # sort by total mistakes, and idle time (for ties)
                player_tuples.sort(key=lambda k: (k[1], k[2]))  # layoff player becomes player 3
                # set new group
                self.set_players([player_tuples[0][0],
                                  player_tuples[1][0],
                                  player_tuples[2][0]])
                print('layoff = weak, REARRANGE')


class Player(BasePlayer):
    pass