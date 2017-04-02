# -*- coding: utf-8 -*-

from flask import request
from modules.helpers import http_code


def schedule_create():
    """
    {
        name: 'job-name',
        date: 'dd/mm/yyyy',
        time: 'HH:MM',
        img:  'docker.io/name'
        envs: [
            {'key': 'value'}
        ]
    }
    """

    put_data = request.get_json(silent=True)

    if not all (k in put_data.keys() for k in ('name', 'img')):
        return http_code(400, 'Bad Request: name and img keys are required.')

    return 'ok'
