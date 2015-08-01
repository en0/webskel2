from flask import jsonify
from flask.views import MethodView
import logging


class ResourceBase(MethodView):
    def dispatch_request(self, *args, **kwargs):
        result = super(ResourceBase, self).dispatch_request(*args, **kwargs)
        if type(result) != tuple:
            _dict = result
            headers = {}
            status = 200
        elif len(result) == 2:
            _dict, status = result
            headers = {}
        elif len(result) == 3:
            _dict, status, headers = result

        body = jsonify(_dict) if _dict else ""
        return body, status, headers

    @classmethod
    def register_route(cls, app):
        _uri = cls.__uri__
        _methods = cls.__method_hints__
        if hasattr(cls, '__pk__'):
            _pk_uri = "{0}<{2}:{1}>".format(_uri, cls.__pk__, cls.__pk_type__)
        else:
            _pk_uri = _uri

        view_fn = cls.as_view("{0}_view".format(cls.__name__.lower()))

        if 'GET' in _methods:
            if hasattr(cls, '__pk__'):
                app.add_url_rule(
                    _uri,
                    defaults={cls.__pk__: None},
                    view_func=view_fn,
                    methods=['GET']
                )
                logging.debug("Register: {0} - [ GET ]".format(_uri))

            app.add_url_rule(
                _pk_uri,
                view_func=view_fn,
                methods=['GET']
            )
            logging.debug("Register: {0} - [ GET ]".format(_pk_uri))

        if 'PUT' in _methods:
            app.add_url_rule(
                _pk_uri,
                view_func=view_fn,
                methods=['PUT']
            )
            logging.debug("Register: {0} - [ PUT ]".format(_pk_uri))

        if 'POST' in _methods:
            if hasattr(cls, '__pk__'):
                app.add_url_rule(
                    _uri,
                    defaults={cls.__pk__: None},
                    view_func=view_fn,
                    methods=['POST']
                )
                logging.debug("Register: {0} - [ POST ]".format(_uri))

            app.add_url_rule(
                _pk_uri,
                view_func=view_fn,
                methods=['POST']
            )
            logging.debug("Register: {0} - [ POST ]".format(_pk_uri))

        if 'DELETE' in _methods:
            app.add_url_rule(
                _pk_uri,
                view_func=view_fn,
                methods=['DELETE']
            )
            logging.debug("Register: {0} - [ DELETE ]".format(_pk_uri))
