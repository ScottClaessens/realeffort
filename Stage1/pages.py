from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Start(Page):

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        # user has 3 minutes to complete as many tasks as possible
        self.participant.vars['expiry'] = time.time() + self.session.config['timer']


class Task(Page):
    form_model = 'player'
    form_fields = ['task']

    timer_text = 'Time left to complete Stage 1:'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry'] - time.time() > 3

    def before_next_page(self):
        if self.timeout_happened is False:
            self.participant.vars['stage1_attempted'] += 1
            num1 = self.session.vars['numbers1'][0][self.subsession.round_number - 1]
            num2 = self.session.vars['numbers1'][1][self.subsession.round_number - 1]
            if self.player.task == num1 + num2:
                self.participant.vars['stage1_correct'] += 1

    def vars_for_template(self):
        num1 = self.session.vars['numbers1'][0][self.subsession.round_number - 1]
        num2 = self.session.vars['numbers1'][1][self.subsession.round_number - 1]
        return {'num1': num1,
                'num2': num2}


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def before_next_page(self):
        self.player.attempted = self.participant.vars['stage1_attempted']
        self.player.correct = self.participant.vars['stage1_correct']

    def vars_for_template(self):
        return {'attempted': self.participant.vars['stage1_attempted'],
                'correct': self.participant.vars['stage1_correct'],
                'earnings': c(self.participant.vars['stage1_correct'])}


page_sequence = [
    Start,
    Task,
    Results,
]
