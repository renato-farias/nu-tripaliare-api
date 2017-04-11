# -*- coding: utf-8 -*-

import datetime

from modules.mongodb import get_jobs_collection

def get_scheduled_jobs():
    pass
    list_schaduled = []
    query = {
        'date_time': {
            '$lte': datetime.datetime.now()
        }
    }
    jobs = get_jobs_collection().find(query)
    return None
    #for j in jobs:
