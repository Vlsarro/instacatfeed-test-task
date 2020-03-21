import config

from flask import Flask, render_template, request

from instagram_api import instagram_web_api_client
from models import process_feed_data
from util import get_exc_data


# application

app = Flask(__name__, template_folder=config.TEMPLATES_PATH)


@app.route('/', methods=['GET'])
def index():
    processed_feed_data = None
    try:
        feed_data = instagram_web_api_client.user_feed(config.INSTAGRAM_USER_ID, count=config.DEFAULT_MEDIA_PER_PAGE,
                                                       extract=True)
        if feed_data:
            processed_feed_data = process_feed_data(config.INSTAGRAM_USER_ID, feed_data)
    except Exception:
        print(f'Error occured: {get_exc_data()}')
    return render_template('index.html', config=config, feed_data=processed_feed_data,
                           instagram_user_id=config.INSTAGRAM_USER_ID, size=request.args.get('size', 'thumb'))


if __name__ == '__main__':
    app_params = {
        'debug': config.DEBUG,
        'threaded': True,
        'host': config.SITE_HOST,
        'port': config.PORT
    }
    app.run(**app_params)
