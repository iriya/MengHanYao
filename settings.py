__author__ = 'iriyadays@gmail.com'

import os
dirname = os.path.dirname(__file__)

STATIC_PATH = os.path.join(dirname, 'assets')
TEMPLATE_PATH = os.path.join(dirname, 'templates')

CLAN_API_SERVER = "http://api-clashofclans.cf"
CLAN_API_HEADERS = {'Content-Type': 'application/json'}
