# -*- coding: utf-8 -*-

import datetime

from modules.helpers import myjsonify
from modules.mongodb import get_jobs_collection


def jobs_list():
    list_jobs = []
    jobs = get_jobs_collection().find({})
    for j in jobs:
        list_jobs.append({
            'name': j['job_name'],
            'when': j.get('date_time', 'no-set'),
            'img':  j['job_img'],
            'envs': {}
        })
        if 'envs' in j.keys() and isinstance(j['envs'], dict) \
                                        and len(j['envs']) > 0:
            for ek, ev in j['envs'].iteritems():
                list_jobs['envs'][ek] = ev

    data = {'jobs': list_jobs}
    return myjsonify(data)
