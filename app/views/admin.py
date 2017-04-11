# -*- coding: utf-8 -*-

import datetime

from modules.helpers import http_code
from modules.mongodb import drop_jobs_collection

def drop_collection():
    drop_jobs_collection()
    return http_code(200, 'Collection Dropped Successfully')
