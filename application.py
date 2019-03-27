from dotenv import load_dotenv
from os import path, getenv
from os.path import dirname, isfile, join

_ENV_FILE = path.dirname(__file__).join('.env')

if path.isfile(_ENV_FILE):
    load_dotenv(dotenv_path = _ENV_FILE)

from apps import create_app

app = create_app(getenv('FLASK_ENV') or 'default')

if __name__ == '__main__':
    ip = '0.0.0.0'
    port = app.config['APP_PORT']
    debug = app.config['DEBUG']

    app.run(
        host = ip, debug = debug, port = port, use_reloader = debug
    )