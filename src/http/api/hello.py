from http import app
from http.api.resource_base import ResourceBase


class Hello(ResourceBase):
    __uri__ = '/api/v<int:major>/hello/'
    __pk__ = 'name'
    __pk_type__ = 'string'
    __method_hints__ = ['GET']

    def get(self, major, name=None):
        _ret = {'Version': major}
        if not name:
            _ret["Message"] = "Hello, world"
        else:
            _ret["Message"] = "Hello, {}".format(name)
        return _ret


Hello.register_route(app)
