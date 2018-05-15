from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Start(Page):
    def is_displayed(self):
        return self.round_number in [1, 31, 61, 91, 121, 151]

    def vars_for_template(self):
        round_number = int((self.round_number + 29) / 30)
        return {'round_number': round_number}


class SetTimerWait(WaitPage):
    def is_displayed(self):
        return self.round_number in [1, 31, 61, 91, 121, 151]

    def after_all_players_arrive(self):
        # GROUP has 3 minutes to complete as many tasks as possible
        for p in self.group.get_players():
            p.participant.vars['expiry'] = None
        self.group.get_player_by_id(1).participant.vars['expiry'] = time.time() + self.session.config['timer']
        self.group.set_round_number()


class WaitForTask1(WaitPage):
    def is_displayed(self):
        order = [1, 2, 3]
        return self.player.display(order)


class WaitForTask2(WaitPage):
    def is_displayed(self):
        order = [2, 3, 1]
        return self.player.display(order)


class WaitForTask3(WaitPage):
    def is_displayed(self):
        order = [3, 1, 2]
        return self.player.display(order)


class Task1(Page):
    form_model = 'player'
    form_fields = ['task']

    timer_text = 'Time left to complete Stage 2:'

    def get_timeout_seconds(self):
        return self.group.timer()

    def is_displayed(self):
        order = [1, 2, 3]
        return self.player.display(order)

    def before_next_page(self):
        if self.timeout_happened is False:
            self.player.task1_before_next_page()

    def vars_for_template(self):
        num1 = self.session.vars['numbers2'][0][self.round_number - 1]
        num2 = self.session.vars['numbers2'][1][self.round_number - 1]
        round_number = self.group.get_player_by_id(1).participant.vars['stage2_round_number']
        return {'num1': num1,
                'num2': num2,
                'round_number': round_number}


class Task2(Page):
    form_model = 'player'
    form_fields = ['task']

    timer_text = 'Time left to complete Stage 2:'

    def get_timeout_seconds(self):
        return self.group.timer()

    def is_displayed(self):
        order = [2, 3, 1]
        return self.player.display(order)

    def before_next_page(self):
        if self.timeout_happened is False:
            self.player.task2_before_next_page()

    def vars_for_template(self):
        order = [1, 2, 3]
        num1 = self.player.num1(order)
        num2 = self.session.vars['numbers2'][2][self.round_number - 1]
        round_number = self.group.get_player_by_id(1).participant.vars['stage2_round_number']
        return {'num1': num1,
                'num2': num2,
                'round_number': round_number}


class Task3(Page):
    form_model = 'player'
    form_fields = ['task']

    timer_text = 'Time left to complete Stage 2:'

    def get_timeout_seconds(self):
        return self.group.timer()

    def is_displayed(self):
        order = [3, 1, 2]
        return self.player.display(order)

    def before_next_page(self):
        if self.timeout_happened is False:
            self.player.task3_before_next_page()

    def vars_for_template(self):
        order = [2, 3, 1]
        num1 = self.player.num1(order)
        num2 = self.session.vars['numbers2'][3][self.round_number - 1]
        round_number = self.group.get_player_by_id(1).participant.vars['stage2_round_number']
        return {'num1': num1,
                'num2': num2,
                'round_number': round_number}


class Results(Page):
    def is_displayed(self):
        return self.round_number in [30, 60, 90, 120, 150, 180]

    def before_next_page(self):
        self.player.save_and_reset_vars()

    def vars_for_template(self):
        p1 = self.group.get_player_by_id(1)
        round_number = self.group.get_player_by_id(1).participant.vars['stage2_round_number']
        return {'attempted_individual': self.participant.vars['stage2_attempted_individual'],
                'correct_individual': self.participant.vars['stage2_correct_individual'],
                'attempted_cycles': p1.participant.vars['stage2_attempted_cycles'],
                'correct_cycles': p1.participant.vars['stage2_correct_cycles'],
                'earnings': c(p1.participant.vars['stage2_correct_cycles']),
                'round_number': round_number}


page_sequence = [
    Start,
    SetTimerWait,
    WaitForTask1,
    Task1,
    WaitForTask2,
    Task2,
    WaitForTask3,
    Task3,
    Results,
]
