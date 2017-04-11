# -*- coding: utf-8 -*-

import datetime

from modules.helpers import myjsonify, objectid_to_apiid
from modules.mongodb import get_jobs_collection

def get_scheduled_jobs(limit=None):
    list_schaduled = []
    query = {
        'date_time': {
            '$lte': datetime.datetime.now()
        }
    }
    jobs = get_jobs_collection().find(query)
    if limit not None:
        jobs = jobs.limit(int(limit))
    for j in jobs:
        list_schaduled.append(
            {
                'id': objectid_to_apiid(str(j['_id'])),
                'name': j['job_name'],
                'envs': {},
                'status': 'scheduled'
            }
        )
        if 'envs' in j.keys() and isinstance(j['envs'], dict) \
                                        and len(j['envs']) > 0:
            for ek, ev in j['envs'].iteritems():
                list_jobs[-1]['envs'][ek] = ev
    data = {'scheduled_jobs': list_schaduled}
    return myjsonify(data)
