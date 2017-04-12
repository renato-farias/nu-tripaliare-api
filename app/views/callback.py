# -*- coding: utf-8 -*-

import app
import datetime

from modules.auth import requires_http_auth
from bson.objectid import ObjectId
from modules.helpers import apiid_to_objectid, http_code
from modules.mongodb import get_jobs_collection

@requires_http_auth
def status_post(appid, status):
    _appid = apiid_to_objectid(appid)
    if status not in app.status:
        http_code(400, 'Wrong status try one of these: %s' % \
                                   str(', '.join(app.status)))

    try:
        get_jobs_collection().update(
            {
                '_id': ObjectId(_appid)
            },
            {
                '$set': {
                    'job_status': status,
                    'updated_at': datetime.datetime.now(),
                }
            }
        )
        http_code(200, 'Job updated successfully.')
    except:
        http_code(500, 'Error while updating job status.')
