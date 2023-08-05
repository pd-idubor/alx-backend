#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user(login_as: int) -> Union[dict, None]:
    """Returns user dict or None if ID is not found """
    if login_as and int(login_as) in users:
        return users[int(login_as)]
    return None


@app.before_request
def before_request():
    """'Gets' user and set as global"""
    g.user = get_user(request.args.get('login_as'))


@app.route('/',  strict_slashes=False)
def index():
    """Welcome pg"""
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """Language translation selection"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    h_locale = request.headers.get('locale')
    if h_locale and h_locale in app.config['LANGUAGES']:
        return h_locale
    return request.accept_languages.best_match(['LANGUAGES'])


if __name__ == '__main__':
    app.run()
