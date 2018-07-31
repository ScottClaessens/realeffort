from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class LayoffWait(WaitPage):
    def is_displayed(self):
        return self.participant.vars['vote'] != 'paycut'

    def after_all_players_arrive(self):
        self.group.layoff()


class Layoff(Page):
    def is_displayed(self):
        return self.participant.vars['vote'] != 'paycut'

    def vars_for_template(self):
        return {'layoff': self.session.config['layoff']}


class Layoff2(Page):
    def is_displayed(self):
        return self.participant.vars['vote'] != 'paycut' and self.player.id_in_group == 3


page_sequence = [
    LayoffWait,
    Layoff,
    Layoff2
]
