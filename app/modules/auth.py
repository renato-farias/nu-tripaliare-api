# -*- coding: utf-8 -*-

import app

from flask import request
from functools import wraps
from modules.helpers import http_code


def requires_http_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if auth is not None and app.cache.get(auth) is not True:
            return http_code(403, 'Access denied. Authorization header is missis or invalid')
        return f(*args, **kwargs)
    return decorated
