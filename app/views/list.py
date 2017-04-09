# -*- coding: utf-8 -*-

import datetime

from flask import jsonify
from modules.mongodb import get_jobs_collection


def jobs_list():
    list_jobs = []
    jobs = get_jobs_collection().find({})
    for j in jobs:
        list_jobs.append(j)
    data = {'jobs': list_jobs}
    return jsonify(data)
