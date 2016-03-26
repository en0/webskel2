import json
from functools import wraps


class structured(object):
    """ Creates a structured return from a dictionary

    This decorator will accept return data and serialize it for return. It will
    set a status code and a content type. By default these values are 200 and
    application/json respectivly. The default serializer is json.

    The calling function can return data in one of four diffrent formats.

    1. return { BODY }, STATUS_CODE, { HEADERS }
    2. return { BODY }, STATUS_CODE
    3. return { BODY }, { HEADERS }
    4. return { BODY }

    Constuctor Arguments:
        serializer:
            Override the default serializer (Optional)

        content_type:
            Override the default content type. (Optional)

        status:
            Override the default status code. (Optional)
    """
    def __init__(self, serializer=None, content_type=None, status=None):
        self._serializer = serializer or json
        self._content_type = content_type or "application/json"
        self._status = status or 200

    def __call__(self, fn):
        @wraps(fn)
        def _wrapper(*args, **kwargs):
            _body, _status, _headers = "", None, {}
            data = fn(*args, **kwargs)

            if type(data) == tuple and len(data) == 2:
                _body, _status = data
                if type(_status) == dict:
                    _headers = _status
                    _status = None

            elif type(data) == tuple and len(data) == 3:
                _body, _status, _headers = data

            elif type(data) == tuple and len(data) == 1:
                _body = data[0]

            elif type(data) != tuple:
                _body = data

            else:
                raise ValueError("Expected content not supplied")

            body = self._serializer.dumps(_body)
            status = _status or self._status
            headers = { "Content-Type": self._content_type }
            headers.update(_headers)

            return body, status, headers

        return _wrapper
