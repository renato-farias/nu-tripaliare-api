# -*- coding: utf-8 -*-

from flask import request
from modules.helpers import http_code
from modules.mongodb import get_jobs_collection


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

    if not isinstance(put_data, dict):
        return http_code(400, 'You should include a json in your request.')

    if not all (k in put_data.keys() for k in ('name', 'img')):
        return http_code(400, 'name and img keys are required.')

    if 'date' in put_data.keys():
        put_date = put_data['date'].split('/')
        if len(put_date) != 3:
            return http_code(400, 'Date required the following format: dd/mm/yyyy.')

    _d = {
        'job_name': put_data['name'],
        'job_img': put_data['img']
    }
    return get_jobs_collection().insert_one(_d).inserted_id
