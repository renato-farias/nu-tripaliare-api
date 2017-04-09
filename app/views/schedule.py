# -*- coding: utf-8 -*-

import datetime

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

    has_date = has_time = False

    put_data = request.get_json(silent=True)

    # checking if the json was parsed correctly.
    if not isinstance(put_data, dict):
        return http_code(400, 'You should include a json in your request.')

    # checking if the dict has the name and img keys. They are the only
    # required fields
    if not all (k in put_data.keys() for k in ('name', 'img')):
        return http_code(400, 'name and img keys are required.')

    _d = {
        'job_name': put_data['name'],
        'job_img': put_data['img']
    }

    # checking the date field is a correct and valid date.
    if 'date' in put_data.keys():
        has_date = True
        put_date = put_data['date'].split('/')
        if len(put_date) != 3:
            return http_code(400, 'Date required the following format: dd/mm/yyyy.')

    if 'time' in put_data.keys():
        has_time = True
        put_time = put_data['time'].split(':')
        if len(put_time) != 2:
            return http_code(400, 'Time required the following format: HH:MM.')

    if has_date and has_time:
        try:
            date_time = datetime.datetime(int(put_date[2]), int(put_date[1]),
                        int(put_date[0]), int(put_time[0]), int(put_time[1]))
        except:
            return http_code(400, 'Date or time was set wrongly. Check and try again.')
        if date_time < datetime.datetime.now():
            return http_code(400, 'The day and time is prior from now.')
        _d['date_time'] = date_time
    elif has_date or has_time:
        return http_code(400, 'Date and Time are required if you set one of them.')

    if 'envs' in put_data.keys():
        if not isinstance(put_data['envs'], list):
            return http_code(400, 'envs field should be a list (array) of keys and values')
        if len(put_data['envs']) > 0:
            envs = []
            for k,v in put_data['envs'].iteritems():
                try:
                    envs.append({
                            k: v
                        })
                except:
                    continue

        _d['envs'] = envs

    return str(get_jobs_collection().insert_one(_d).inserted_id)
