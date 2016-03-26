from flask import Flask, redirect
from libs import Config
from webapp.ui import mod as ui_mod
from webapp.api import mod as api_mod
import logging


app = Flask(__name__)
with app.app_context():
    app.iniconfig = Config()
    app.iniconfig.read("config.ini")


logging.basicConfig(
    level=app.iniconfig.log_level,
    format=app.iniconfig.log_format,
    datefmt=app.iniconfig.log_datefmt,
    path=app.iniconfig.log_path
)


app.register_blueprint(ui_mod)
app.register_blueprint(api_mod)


@app.route('/')
def _():
    return redirect('/web')


__all__ = [
    'app',
]
