# -*- coding: utf-8 -*-

from flask import jsonify

def http_code(code, msg=''):
    response = jsonify({'code': code,'message': msg})
    response.status_code = code
    return response
