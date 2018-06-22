from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import time


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
    def timer(self):
        return self.get_player_by_id(1).participant.vars['expiry'] - time.time()

    def set_round_number(self):
        self.get_player_by_id(1).participant.vars['stage2_round_number'] = int((self.round_number + 29) / 30)


class Player(BasePlayer):
    task = models.IntegerField(
        min=20,
        max=396
    )

    attempted_individual = models.IntegerField()
    correct_individual = models.IntegerField()
    attempted_cycles = models.IntegerField()
    correct_cycles = models.IntegerField()

    def task1_before_next_page(self):
        self.participant.vars['stage2_attempted_individual'] += 1
        num1 = self.session.vars['numbers2'][0][self.round_number - 1]
        num2 = self.session.vars['numbers2'][1][self.round_number - 1]
        if self.task == num1 + num2:
            self.participant.vars['stage2_correct_individual'] += 1
            self.group.get_player_by_id(1).participant.vars['stage2_currentcyclecorrect?'] = True
        else:
            self.group.get_player_by_id(1).participant.vars['stage2_currentcyclecorrect?'] = False

    def task2_before_next_page(self):
        self.participant.vars['stage2_attempted_individual'] += 1
        if self.round_number in range(1, 31) or self.round_number in range(91, 121):
            num1 = self.group.get_player_by_id(1).task
        elif self.round_number in range(31, 61) or self.round_number in range(121, 151):
            num1 = self.group.get_player_by_id(2).task
        else:
            num1 = self.group.get_player_by_id(3).task
        num2 = self.session.vars['numbers2'][2][self.round_number - 1]
        if self.task == num1 + num2:
            self.participant.vars['stage2_correct_individual'] += 1
            if self.group.get_player_by_id(1).participant.vars['stage2_currentcyclecorrect?'] is True:
                self.group.get_player_by_id(1).participant.vars['stage2_currentcyclecorrect?'] = True
            else:
                self.group.get_player_by_id(1).participant.vars['stage2_currentcyclecorrect?'] = False
        else:
            self.group.get_player_by_id(1).participant.vars['stage2_currentcyclecorrect?'] = False


    def task3_before_next_page(self):
        self.participant.vars['stage2_attempted_individual'] += 1
        self.group.get_player_by_id(1).participant.vars['stage2_attempted_cycles'] += 1
        if self.round_number in range(1, 31) or self.round_number in range(91, 121):
            num1 = self.group.get_player_by_id(2).task
        elif self.round_number in range(31, 61) or self.round_number in range(121, 151):
            num1 = self.group.get_player_by_id(3).task
        else:
            num1 = self.group.get_player_by_id(1).task
        num2 = self.session.vars['numbers2'][3][self.round_number - 1]
        if self.task == num1 + num2:
            self.participant.vars['stage2_correct_individual'] += 1
            if self.group.get_player_by_id(1).participant.vars['stage2_currentcyclecorrect?'] is True:
                self.group.get_player_by_id(1).participant.vars['stage2_currentcyclecorrect?'] = True
            else:
                self.group.get_player_by_id(1).participant.vars['stage2_currentcyclecorrect?'] = False
        else:
            self.group.get_player_by_id(1).participant.vars['stage2_currentcyclecorrect?'] = False
        if self.group.get_player_by_id(1).participant.vars['stage2_currentcyclecorrect?'] is True:
            self.group.get_player_by_id(1).participant.vars['stage2_correct_cycles'] += 1

    def display(self, order):
        if self.group.get_player_by_id(1).participant.vars['expiry'] - time.time() > 3:
            if self.round_number in range(1, 31) or self.round_number in range(91, 121):
                return self.id_in_group == order[0]
            elif self.round_number in range(31, 61) or self.round_number in range(121, 151):
                return self.id_in_group == order[1]
            else:
                return self.id_in_group == order[2]
        else:
            return False

    def num1(self, order):
        if self.round_number in range(1, 31) or self.round_number in range(91, 121):
            return self.group.get_player_by_id(order[0]).task
        elif self.round_number in range(31, 61) or self.round_number in range(121, 151):
            return self.group.get_player_by_id(order[1]).task
        else:
            return self.group.get_player_by_id(order[2]).task

    def save_and_reset_vars(self):
        p1 = self.group.get_player_by_id(1)
        # Add to payoffs
        self.payoff = c(30) * (p1.participant.vars['stage2_correct_cycles']//2)
        # Save vars
        self.attempted_individual = self.participant.vars['stage2_attempted_individual']
        self.correct_individual = self.participant.vars['stage2_correct_individual']
        self.attempted_cycles = p1.participant.vars['stage2_attempted_cycles']
        self.correct_cycles = p1.participant.vars['stage2_correct_cycles']
        # Reset vars
        self.participant.vars['stage2_attempted_individual'] = 0
        self.participant.vars['stage2_correct_individual'] = 0
        p1.participant.vars['stage2_attempted_cycles'] = 0
        p1.participant.vars['stage2_correct_cycles'] = 0