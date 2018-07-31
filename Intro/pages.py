from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Intro(Page):
    pass


page_sequence = [
    Intro,
]
