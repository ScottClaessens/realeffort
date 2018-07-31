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

# set variables for ALL treatment types
timer = 180  # in seconds
stage1_piecerate = 2  # thalers for each correct question


SESSION_CONFIGS = [
    {
       'name': 'realeffort1',
       'display_name': "Treatment 1 - Baseline (n=3); Baseline (n=3)",
       'num_demo_participants': 3,
       'use_browser_bots': False,
       'app_sequence': ['Intro',
                        'Stage1',
                        'Stage2_n3',
                        'Stage3_n3'],
       'timer': timer,
       'stage1_piecerate': stage1_piecerate,
       'stage3_piecerate': 30,
       'stage3_requiredcycles': 2
    },
    {
       'name': 'realeffort2',
       'display_name': "Treatment 2 - Baseline (n=3); Pay cut, workload (n=3)",
       'num_demo_participants': 3,
       'use_browser_bots': False,
       'app_sequence': ['Intro',
                        'Stage1',
                        'Stage2_n3',
                        'Stage3_n3'],
       'timer': timer,
       'stage1_piecerate': stage1_piecerate,
       'stage3_piecerate': 30,
       'stage3_requiredcycles': 3
    },
    {
       'name': 'realeffort3',
       'display_name': "Treatment 3 - Baseline (n=3); Layoff - random (n=2)",
       'num_demo_participants': 3,
       'use_browser_bots': False,
       'app_sequence': ['Intro',
                        'Stage1',
                        'Stage2_n3',
                        'Layoff',
                        'Stage3_n2layoff'],
       'timer': timer,
       'stage1_piecerate': stage1_piecerate,
       'layoff': 'random',
       'stage3_piecerate': 30,
       'stage3_requiredcycles': 3
    },
    {
        'name': 'realeffort4',
        'display_name': "Treatment 4 - Baseline (n=3); Layoff - weak (n=2)",
        'num_demo_participants': 3,
        'use_browser_bots': False,
        'app_sequence': ['Intro',
                         'Stage1',
                         'Stage2_n3',
                         'Layoff',
                         'Stage3_n2layoff'],
        'timer': timer,
        'stage1_piecerate': stage1_piecerate,
        'layoff': 'weak',
        'stage3_piecerate': 30,
        'stage3_requiredcycles': 3
    },
    {
       'name': 'realeffort5',
       'display_name': "Treatment 5 - Baseline (n=2); Pay cut, workload (n=2)",
       'num_demo_participants': 2,
       'use_browser_bots': False,
       'app_sequence': ['Intro',
                        'Stage1',
                        'Stage2_n2',
                        'Stage3_n2'],
       'timer': timer,
       'stage1_piecerate': stage1_piecerate,
       'stage3_piecerate': 30,
       'stage3_requiredcycles': 3
    },
    {
       'name': 'realeffort6',
       'display_name': "Treatment 6 - Baseline (n=3); Pay cut, piece rate (n=3)",
       'num_demo_participants': 3,
       'use_browser_bots': False,
       'app_sequence': ['Intro',
                        'Stage1',
                        'Stage2_n3',
                        'Stage3_n3'],
       'timer': timer,
       'stage1_piecerate': stage1_piecerate,
       'stage3_piecerate': 20,
       'stage3_requiredcycles': 2
    },
    {
       'name': 'realeffort7',
       'display_name': "Treatment 7 - Baseline (n=3); Vote between layoff (random) and pay cut, piece rate (n=3)",
       'num_demo_participants': 3,
       'use_browser_bots': False,
       'app_sequence': ['Intro',
                        'Stage1',
                        'Stage2_n3',
                        'Voting',
                        'Stage3_n3',
                        'Layoff',
                        'Stage3_n2layoff'],
       'timer': timer,
       'stage1_piecerate': stage1_piecerate,
       'layoff': 'random',
       'stage3_piecerate': 20,
       'stage3_requiredcycles': 2
    },
    {
       'name': 'realeffort8',
       'display_name': "Treatment 8 - Baseline (n=3); Vote between layoff (weak) and pay cut, piece rate (n=3)",
       'num_demo_participants': 3,
       'use_browser_bots': False,
       'app_sequence': ['Intro',
                        'Stage1',
                        'Stage2_n3',
                        'Voting',
                        'Stage3_n3',
                        'Layoff',
                        'Stage3_n2layoff'],
       'timer': timer,
       'stage1_piecerate': stage1_piecerate,
       'layoff': 'weak',
       'stage3_piecerate': 20,
       'stage3_requiredcycles': 2
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'thalers'

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

SENTRY_DSN = 'http://d606c64efb5d449d9ac450ef47fef1b0:1f312687dcc6423fa67a65d3b78782dc@sentry.otree.org/143'

# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_TITLE = 'Real-Effort Workers'
DEMO_PAGE_INTRO_HTML = 'Click on a treatment type to play a demo.'

# don't share this with anybody.
SECRET_KEY = '(b=k%jx^!kh08ifkaj()$#x&*sm(6u4=23pp1aw_vg-_hio*s@'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = [
    'otree',
]
