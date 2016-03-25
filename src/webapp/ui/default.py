from . import mod
from flask import abort, render_template
from jinja2.exceptions import TemplateNotFound


@mod.route('/')
@mod.route('/<path:path>')
def default_route(path="index.html"):
    try:
        return render_template(path)
    except TemplateNotFound:
        abort(404)
