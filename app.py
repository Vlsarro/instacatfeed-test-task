import hashlib
import string
import random

import config

from flask import Flask, render_template, request
from instagram_web_api import Client

from cat_classifier import CatPipeline
from models import process_feed_data
from util import get_exc_data


# application

app = Flask(__name__, template_folder=config.TEMPLATES_PATH)

# Instagram API without authentication


class InstagramClient(Client):

    @staticmethod
    def _extract_rhx_gis(html):
        options = string.ascii_lowercase + string.digits
        text = ''.join([random.choice(options) for _ in range(8)])
        return hashlib.md5(text.encode()).hexdigest()


instagram_web_api = InstagramClient(auto_patch=True, drop_incompat_keys=False)

# Cat classifier

# cat_classifier = CatPipeline()


@app.route('/', methods=['GET'])
def index():
    cleaned_feed_data = None
    try:
        feed_data = instagram_web_api.user_feed(config.INSTAGRAM_USER_ID, count=config.DEFAULT_MEDIA_PER_PAGE,
                                                extract=True)
        cleaned_feed_data = process_feed_data(feed_data)
    except Exception:
        print(f'Error occured: {get_exc_data()}')
    return render_template('index.html', config=config, feed_data=cleaned_feed_data,
                           instagram_user_id=config.INSTAGRAM_USER_ID, size=request.args.get('size', 'thumb'))


if __name__ == '__main__':
    app_params = {
        'debug': config.DEBUG,
        'threaded': True,
        'host': config.SITE_HOST,
        'port': config.PORT
    }
    app.run(**app_params)
