import shutil
import sys
import traceback
import requests


__all__ = ('get_exc_data', 'save_file_from_url')


def get_exc_data():
    exc_type, exc, tb = sys.exc_info()
    return ''.join(traceback.format_exception(exc_type, exc, tb))


def save_file_from_url(url, filepath):
    response = requests.get(url, stream=True)
    with open(filepath, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
