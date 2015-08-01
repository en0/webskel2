from flask import Flask, abort
import config
import logging

app = Flask(__name__)

app.config.from_object(config.Default)

try:
    app.config.from_envvar('SERVICE_CONFIG')
except RuntimeError:
    app.config.from_object(config.Debug)

logging_config = dict(
    level=app.config.get('LOG_LEVEL'),
    format=app.config.get('LOG_FORMAT')
)

if 'LOG_FILE' in app.config:
    logging_config['filename'] = app.config.get('LOG_FILE')

logging.basicConfig(**logging_config)

import http.midware
import http.api
import http.ui

__all__ = [
    'app',
    'abort'
]
