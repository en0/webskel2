from flask import render_template
from http import app, abort
from jinja2.exceptions import TemplateNotFound


@app.route('/')
@app.route('/<path:path>')
def default_route(path="index.html"):
    try:
        return render_template(path)
    except TemplateNotFound:
        abort(404)
