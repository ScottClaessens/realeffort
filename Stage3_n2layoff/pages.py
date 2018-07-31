from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Intro(Page):
    def is_displayed(self):
        return self.participant.vars['vote'] != 'paycut' and self.round_number == 1 and self.player.id_in_group != 3

    def vars_for_template(self):
        return {'stage3_piecerate': self.session.config['stage3_piecerate'],
                'stage3_requiredcycles': self.session.config['stage3_requiredcycles']}


class Start(Page):
    def is_displayed(self):
        return self.participant.vars['vote'] != 'paycut' and self.round_number in [1, 31, 61, 91, 121, 151] \
               and self.player.id_in_group != 3

    def before_next_page(self):
        # moved from after_all_players_arrive, as it does not run now
        self.player.participant.vars['stage3_attempted_individual'] = 0
        self.player.participant.vars['stage3_correct_individual'] = 0
        if self.player.id_in_group == 1:
            self.player.participant.vars['stage3_attempted_cycles'] = 0
            self.player.participant.vars['stage3_correct_cycles'] = 0
            self.player.participant.vars['stage3_round_number'] = int((self.round_number + 29) / 30)
        # set timer here, will stick for last player to set it
        self.group.get_player_by_id(1).participant.vars['expiry'] = time.time() + self.session.config['timer']

    def vars_for_template(self):
        round_number = int((self.round_number + 29) / 30)
        return {'round_number': round_number,
                'stage3_piecerate': self.session.config['stage3_piecerate'],
                'stage3_requiredcycles': self.session.config['stage3_requiredcycles']}


class SetTimerWait(WaitPage):
    def is_displayed(self):
        return self.participant.vars['vote'] != 'paycut' and self.round_number in [1, 31, 61, 91, 121, 151] \
               and self.player.id_in_group != 3


class WaitForTask1(WaitPage):
    template_name = 'Stage3_n2layoff/MyWaitPage.html'

    def is_displayed(self):
        if self.participant.vars['vote'] == 'paycut':
            return False
        else:
            order = [1, 2]
            if self.player.id_in_group == 3:
                return False
            else:
                return self.player.display(order)

    def vars_for_template(self):
        return {'expiry': self.group.timer()}


class WaitForTask2(WaitPage):
    template_name = 'Stage3_n2layoff/MyWaitPage.html'

    def is_displayed(self):
        if self.participant.vars['vote'] == 'paycut':
            return False
        else:
            order = [2, 1]
            if self.player.id_in_group == 3:
                return False
            else:
                return self.player.display(order)

    def vars_for_template(self):
        return {'expiry': self.group.timer()}


class Task1(Page):
    form_model = 'player'
    form_fields = ['task']

    timer_text = 'Remaining time:'

    def get_timeout_seconds(self):
        return self.group.timer()

    def is_displayed(self):
        if self.participant.vars['vote'] == 'paycut':
            return False
        else:
            order = [1, 2]
            if self.player.id_in_group == 3:
                return False
            else:
                return self.player.display(order)

    def before_next_page(self):
        if self.timeout_happened is False:
            self.player.task1_before_next_page()

    def vars_for_template(self):
        num1 = self.session.vars['numbers3'][0][self.round_number - 1]
        num2 = self.session.vars['numbers3'][1][self.round_number - 1]
        round_number = self.group.get_player_by_id(1).participant.vars['stage3_round_number']
        return {'num1': num1,
                'num2': num2,
                'round_number': round_number}


class Task2(Page):
    form_model = 'player'
    form_fields = ['task']

    timer_text = 'Remaining time:'

    def get_timeout_seconds(self):
        return self.group.timer()

    def is_displayed(self):
        if self.participant.vars['vote'] == 'paycut':
            return False
        else:
            order = [2, 1]
            if self.player.id_in_group == 3:
                return False
            else:
                return self.player.display(order)

    def before_next_page(self):
        if self.timeout_happened is False:
            self.player.task2_before_next_page()

    def vars_for_template(self):
        order = [1, 2]
        num1 = self.player.num1(order)
        num2 = self.session.vars['numbers3'][2][self.round_number - 1]
        round_number = self.group.get_player_by_id(1).participant.vars['stage3_round_number']
        return {'num1': num1,
                'num2': num2,
                'round_number': round_number}


class Results(Page):
    def is_displayed(self):
        if self.participant.vars['vote'] == 'paycut':
            return False
        else:
            return self.round_number in [30, 60, 90, 120, 150, 180] and self.player.id_in_group is not 3

    def before_next_page(self):
        self.player.save_and_reset_vars()
        if self.round_number is 180:
            self.player.calculate_idle_time()

    def vars_for_template(self):
        p1 = self.group.get_player_by_id(1)
        round_number = self.group.get_player_by_id(1).participant.vars['stage3_round_number']
        return {'attempted_individual': self.participant.vars['stage3_attempted_individual'],
                'correct_individual': self.participant.vars['stage3_correct_individual'],
                'attempted_cycles': p1.participant.vars['stage3_attempted_cycles'],
                'correct_cycles': p1.participant.vars['stage3_correct_cycles'],
                'earnings': c(self.session.config['stage3_piecerate']) *
                            (p1.participant.vars['stage3_correct_cycles']//self.session.config['stage3_requiredcycles']),
                'round_number': round_number}


page_sequence = [
    Intro,
    Start,
    SetTimerWait,
    WaitForTask1,
    Task1,
    WaitForTask2,
    Task2,
    Results,
]
