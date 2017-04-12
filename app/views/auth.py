# -*- coding: utf-8 -*-

import app
import datetime

from flask import request
from base64 import b64encode

from modules.helpers import myjsonify

api_auth_user = 'api'
api_auth_pass = 'Qui<coo9'


def auth_post():
    auth = request.get_json(silent=True)

    if not all (k in auth.keys() for k in ('user', 'pass')):
        return http_code(400, 'user and pass keys are required.')

    if auth['user'] == api_auth_user and auth['pass'] == api_auth_pass:
        authorization = b64encode(datetime.datetime.now())
        login = {
            'authorizarion': authorization
        }
        app.cache.set(authorization, True, timeout=60*30)
        return myjsonify(login)

    return http_code(404, 'username or password are invalid.')
