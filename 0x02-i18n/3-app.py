#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/',  strict_slashes=False)
def index():
    """Welcome pg"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """Language translation selection"""
    return request.accept_languages.best_match(['LANGUAGES'])


if __name__ == '__main__':
    app.run()
