import os

SITE_HOST = '0.0.0.0'
PORT = 5000

DEBUG = True

ENCODING = 'utf-8'

ROOT_PATH = os.path.dirname(__file__)
TEMPLATES_PATH = os.path.join(ROOT_PATH, 'templates')
SAVED_DATA_PATH = os.path.join(ROOT_PATH, 'saved_data')
INSTAGRAM_USER_DATA_PATH = os.path.join(ROOT_PATH, 'user_data.json')

DEFAULT_MEDIA_PER_PAGE = 10
STATIC_RHS_GIS = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
