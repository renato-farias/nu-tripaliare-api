# -*- coding: utf-8 -*-

from flask import jsonify

def http_code(code, msg='', info={}):
    data = {'code': code,'message': msg}
    if len(info) > 0:
        data.update(info)
    response = jsonify(data)
    response.status_code = code
    return response
