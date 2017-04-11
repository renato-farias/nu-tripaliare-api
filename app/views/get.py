# -*- coding: utf-8 -*-

import datetime

from modules.helpers import myjsonify, objectid_to_apiid
from modules.mongodb import get_jobs_collection

def get_scheduled_jobs(limit=None):
    list_scheduled = []
    query = {
        'date_time': {
            '$lte': datetime.datetime.now()
        }
    }
    jobs = get_jobs_collection().find(query)
    if limit is not None:
        jobs = jobs.limit(int(limit))
    for j in jobs:
        list_scheduled.append(
            {
                'id': objectid_to_apiid(str(j['_id'])),
                'name': j['job_name'],
                'envs': {},
                'status': j['job_status']
            }
        )
        if 'envs' in j.keys() and isinstance(j['envs'], dict) \
                                        and len(j['envs']) > 0:
            for ek, ev in j['envs'].iteritems():
                list_scheduled[-1]['envs'][ek] = ev
    data = {'scheduled_jobs': list_scheduled}
    return myjsonify(data)
