from . import mod
from flask import current_app
from lib.resources.decorators import structured


@mod.route('/<string:ver>/hello/<string:name>')
@structured()
def _(ver, name):
    return {
        "Message": "Hello, {}".format(name),
        "Version": ver,
        "log_level": current_app.iniconfig.log_level
    }
