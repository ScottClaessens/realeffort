from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import time
from otree.models_concrete import PageCompletion


author = 'Scott Claessens - University of Auckland'

doc = """
Real-Effort Task - Stage 3
"""


class Constants(BaseConstants):
    name_in_url = 'Stage3_n2'
    players_per_group = 2
    num_rounds = 180


class Subsession(BaseSubsession):
    def creating_session(self):
        self.session.vars['numbers3'] = []
        for n in range(12, 20):
            random.seed(n)
            self.session.vars['numbers3'].append(random.sample(list(range(10, 100)) * 3, 180))
        for p in self.get_players():
            p.participant.vars['stage3_attempted_individual'] = 0
            p.participant.vars['stage3_correct_individual'] = 0
            p.participant.vars['stage3_total_mistakes_individual'] = 0
        for g in self.get_groups():
            p1 = g.get_player_by_id(1)
            p1.participant.vars['stage3_attempted_cycles'] = 0
            p1.participant.vars['stage3_correct_cycles'] = 0
            p1.participant.vars['stage3_currentcyclecorrect?'] = False


class Group(BaseGroup):
    def timer(self):
        return self.get_player_by_id(1).participant.vars['expiry'] - time.time()

    def set_round_number(self):
        self.get_player_by_id(1).participant.vars['stage3_round_number'] = int((self.round_number + 29) / 30)


class Player(BasePlayer):
    task = models.IntegerField(
        min=20,
        max=396
    )

    task2 = models.IntegerField(
        min=20,
        max=396
    )

    task3 = models.IntegerField(
        min=20,
        max=396
    )

    attempted_individual = models.IntegerField()
    correct_individual = models.IntegerField()
    attempted_cycles = models.IntegerField()
    correct_cycles = models.IntegerField()
    idle_time = models.IntegerField()

    def task1_before_next_page(self):
        self.participant.vars['stage3_attempted_individual'] += 1
        num1 = self.session.vars['numbers3'][0][self.round_number - 1]
        num2 = self.session.vars['numbers3'][1][self.round_number - 1]
        if self.task == num1 + num2:
            self.participant.vars['stage3_correct_individual'] += 1
            self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = True
        else:
            self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = False

    def task2_before_next_page(self):
        self.participant.vars['stage3_attempted_individual'] += 1
        if self.round_number in range(1, 31) or self.round_number in range(61, 91) or self.round_number in range(
                121, 151):
            num1 = self.group.get_player_by_id(1).task
        else:
            num1 = self.group.get_player_by_id(2).task
        num2 = self.session.vars['numbers3'][2][self.round_number - 1]
        if self.task == num1 + num2:
            self.participant.vars['stage3_correct_individual'] += 1
            if self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] is True:
                self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = True
            else:
                self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = False
        else:
            self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = False

    def task3_before_next_page(self):
        self.participant.vars['stage3_attempted_individual'] += 1
        self.group.get_player_by_id(1).participant.vars['stage3_attempted_cycles'] += 1
        if self.round_number in range(1, 31) or self.round_number in range(61, 91) or self.round_number in range(
                121, 151):
            num1 = self.group.get_player_by_id(2).task
        else:
            num1 = self.group.get_player_by_id(1).task
        num2 = self.session.vars['numbers3'][3][self.round_number - 1]
        if self.task2 == num1 + num2:
            self.participant.vars['stage3_correct_individual'] += 1
            if self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] is True:
                self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = True
            else:
                self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = False
        else:
            self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = False
        if self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] is True:
            self.group.get_player_by_id(1).participant.vars['stage3_correct_cycles'] += 1

    def task4_before_next_page(self):
        self.participant.vars['stage3_attempted_individual'] += 1
        num1 = self.session.vars['numbers3'][4][self.round_number - 1]
        num2 = self.session.vars['numbers3'][5][self.round_number - 1]
        if self.task2 == num1 + num2:
            self.participant.vars['stage3_correct_individual'] += 1
            self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = True
        else:
            self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = False

    def task5_before_next_page(self):
        self.participant.vars['stage3_attempted_individual'] += 1
        if self.round_number in range(1, 31) or self.round_number in range(61, 91) or self.round_number in range(
                121, 151):
            num1 = self.group.get_player_by_id(2).task2
        else:
            num1 = self.group.get_player_by_id(1).task2
        num2 = self.session.vars['numbers3'][6][self.round_number - 1]
        if self.task3 == num1 + num2:
            self.participant.vars['stage3_correct_individual'] += 1
            if self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] is True:
                self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = True
            else:
                self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = False
        else:
            self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = False

    def task6_before_next_page(self):
        self.participant.vars['stage3_attempted_individual'] += 1
        self.group.get_player_by_id(1).participant.vars['stage3_attempted_cycles'] += 1
        if self.round_number in range(1, 31) or self.round_number in range(61, 91) or self.round_number in range(
                121, 151):
            num1 = self.group.get_player_by_id(1).task3
        else:
            num1 = self.group.get_player_by_id(2).task3
        num2 = self.session.vars['numbers3'][7][self.round_number - 1]
        if self.task3 == num1 + num2:
            self.participant.vars['stage3_correct_individual'] += 1
            if self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] is True:
                self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = True
            else:
                self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = False
        else:
            self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] = False
        if self.group.get_player_by_id(1).participant.vars['stage3_currentcyclecorrect?'] is True:
            self.group.get_player_by_id(1).participant.vars['stage3_correct_cycles'] += 1

    def display(self, order):
        if self.group.get_player_by_id(1).participant.vars['expiry'] - time.time() > 3:
            if self.round_number in range(1, 31) or self.round_number in range(61, 91) or self.round_number in range(
                    121, 151):
                return self.id_in_group == order[0]
            else:
                return self.id_in_group == order[1]
        else:
            return False

    def num1(self, order, task):
        if self.round_number in range(1, 31) or self.round_number in range(61, 91) or self.round_number in range(
                121, 151):
            if task == 1:
                return self.group.get_player_by_id(order[0]).task
            elif task == 2:
                return self.group.get_player_by_id(order[0]).task2
            elif task == 3:
                return self.group.get_player_by_id(order[0]).task3
        else:
            if task == 1:
                return self.group.get_player_by_id(order[1]).task
            elif task == 2:
                return self.group.get_player_by_id(order[1]).task2
            elif task == 3:
                return self.group.get_player_by_id(order[1]).task3

    def save_and_reset_vars(self):
        # Add to payoffs
        self.payoff = c(30) * (self.group.get_player_by_id(1).participant.vars['stage3_correct_cycles']//2)
        # Save vars
        self.attempted_individual = self.participant.vars['stage3_attempted_individual']
        self.correct_individual = self.participant.vars['stage3_correct_individual']
        self.attempted_cycles = self.group.get_player_by_id(1).participant.vars['stage3_attempted_cycles']
        self.correct_cycles = self.group.get_player_by_id(1).participant.vars['stage3_correct_cycles']
        # Overall participant var
        self.participant.vars['stage3_total_mistakes_individual'] += \
            self.participant.vars['stage3_attempted_individual'] - self.participant.vars['stage3_correct_individual']

    def calculate_idle_time(self):
        waiting_pages = [
            'WaitForTask1',
            'WaitForTask2',
            'WaitForTask3',
            'WaitForTask4',
            'WaitForTask5',
            'WaitForTask6'
        ]
        wp_sec = sum(PageCompletion.objects.filter(participant=self.participant,
                                                   page_name__in=waiting_pages).values_list(
            'seconds_on_page',
            flat=True))
        self.idle_time = wp_sec
        self.participant.vars['stage3_idletime'] = wp_sec