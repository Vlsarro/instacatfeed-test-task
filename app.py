import config

from flask import Flask, render_template, request

from instagram_api import instagram_web_api_client
from models import process_feed_data, load_instagram_user_data
from util import get_exc_data

# TODO: add caching, add logging insted of print expressions, add loading images from accounts that user is following
# expand custom exceptions and their handling, add tests

app = Flask(__name__, template_folder=config.TEMPLATES_PATH)


@app.route('/', methods=['GET'])
def index():
    processed_feed_data = None
    instagram_user_id = load_instagram_user_data(config.INSTAGRAM_USER_DATA_PATH)
    try:
        feed_data = instagram_web_api_client.user_feed(instagram_user_id, count=config.DEFAULT_MEDIA_PER_PAGE,
                                                       extract=True)
        if feed_data:
            processed_feed_data = process_feed_data(instagram_user_id, feed_data)
    except Exception:
        print(f'Error occured: {get_exc_data()}')
    return render_template('index.html', config=config, feed_data=processed_feed_data,
                           instagram_user_id=instagram_user_id, size=request.args.get('size', 'thumb'))


if __name__ == '__main__':
    app_params = {
        'debug': config.DEBUG,
        'threaded': True,
        'host': config.SITE_HOST,
        'port': config.PORT
    }
    app.run(**app_params)
