# -*- coding: utf-8 -*-

import datetime

from modules.auth import requires_http_auth
from modules.helpers import myjsonify, objectid_to_apiid
from modules.mongodb import get_jobs_collection

@requires_http_auth
def jobs_list():
    list_jobs = []
    jobs = get_jobs_collection().find({})
    for j in jobs:

        _when = j.get('date_time', 'no-set')
        if isinstance(_when, datetime.datetime):
            _when = _when.strftime('%d/%m/%Y - %H:%M')

        list_jobs.append({
            'id': objectid_to_apiid(str(j['_id'])),
            'name': j['job_name'],
            'when': _when,
            'img':  j['job_img'],
            'envs': {},
            'status': 'scheduled'
        })
        if 'envs' in j.keys() and isinstance(j['envs'], dict) \
                                        and len(j['envs']) > 0:
            for ek, ev in j['envs'].iteritems():
                list_jobs[-1]['envs'][ek] = ev

    data = {'jobs': list_jobs}
    return myjsonify(data)
