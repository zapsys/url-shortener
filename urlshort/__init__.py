from flask import Flask
import random
import string


def key_generator(size=20, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = key_generator()

    from . import urlshort

    app.register_blueprint(urlshort.bp)

    return app
