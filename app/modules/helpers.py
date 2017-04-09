# -*- coding: utf-8 -*-

from flask import make_response, jsonify

def http_code(code, msg='', info={}):
    data = {'code': code,'message': msg}
    if len(info) > 0:
        data.update(info)
    response = jsonify(data)
    response.status_code = code
    return response


def myjsonify(data=None, code=200, headers=None):
    data = [] if not data else data
    r = make_response(json.dumps(data,
        indent=2,
        sort_keys=True,
        ensure_ascii=False,
        encoding='utf8') + '\n',
        code)
    r.headers['Content-Type'] = 'application/json; charset=utf-8'
    return r
