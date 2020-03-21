import config
from flask import Flask

# application

app = Flask(__name__, template_folder=config.TEMPLATES_PATH)


if __name__ == '__main__':
    app_params = {
        'debug': config.DEBUG,
        'threaded': True,
        'host': config.SITE_HOST,
        'port': config.PORT
    }
    app.run(**app_params)
