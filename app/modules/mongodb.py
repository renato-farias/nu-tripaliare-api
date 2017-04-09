# -*- coding: UTF-8 -*-

import pymongo

def get_mongodb():
    try:
        c = pymongo.MongoClient('33.33.33.43', 27107)
        return c['nu-tripaliare']
    except:
        return None

def get_jobs_collection():
    c = get_mongodb()
    if c:
        return c['jobs']
    return None
