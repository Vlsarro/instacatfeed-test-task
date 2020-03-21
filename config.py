import os

SITE_HOST = '0.0.0.0'
PORT = 5000

DEBUG = True

ENCODING = 'utf-8'

ROOT_PATH = os.path.dirname(__file__)
TEMPLATES_PATH = os.path.join(ROOT_PATH, 'templates')

DEFAULT_MEDIA_PER_PAGE = 10
