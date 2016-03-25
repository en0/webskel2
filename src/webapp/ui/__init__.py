from flask import Blueprint, render_template

mod = Blueprint(
    'web',
    __name__,
    url_prefix="/web",
    template_folder="templates",
    static_folder="static"
)

import default
