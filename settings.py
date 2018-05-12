from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
       'name': 'realeffort1',
       'display_name': "Real-Effort Experiment - Treatment 1",
       'num_demo_participants': 3,
       'app_sequence': ['Stage1'],
       'treatment': 1
    },
    {
       'name': 'realeffort2',
       'display_name': "Real-Effort Experiment - Treatment 2",
       'num_demo_participants': 3,
       'app_sequence': ['Stage1'],
       'treatment': 2
    },
    {
       'name': 'realeffort3',
       'display_name': "Real-Effort Experiment - Treatment 3",
       'num_demo_participants': 3,
       'app_sequence': ['Stage1'],
       'treatment': 3
    },
    {
       'name': 'realeffort4',
       'display_name': "Real-Effort Experiment - Treatment 4",
       'num_demo_participants': 3,
       'app_sequence': ['Stage1'],
       'treatment': 4
    },
    {
       'name': 'realeffort5',
       'display_name': "Real-Effort Experiment - Treatment 5",
       'num_demo_participants': 3,
       'app_sequence': ['Stage1'],
       'treatment': 5
    },
    {
       'name': 'realeffort6',
       'display_name': "Real-Effort Experiment - Treatment 6",
       'num_demo_participants': 3,
       'app_sequence': ['Stage1'],
       'treatment': 6
    },
    {
       'name': 'realeffort7',
       'display_name': "Real-Effort Experiment - Treatment 7",
       'num_demo_participants': 3,
       'app_sequence': ['Stage1'],
       'treatment': 7
    },
    {
       'name': 'realeffort8',
       'display_name': "Real-Effort Experiment - Treatment 8",
       'num_demo_participants': 3,
       'app_sequence': ['Stage1'],
       'treatment': 8
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

# don't share this with anybody.
SECRET_KEY = '(b=k%jx^!kh08ifkaj()$#x&*sm(6u4=23pp1aw_vg-_hio*s@'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']