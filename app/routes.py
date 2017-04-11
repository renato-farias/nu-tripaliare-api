# -*- coding: utf-8 -*-

from flask import Blueprint, current_app

from views.list import jobs_list
from views.admin import drop_collection
from views.schedule import schedule_create

routes = Blueprint('routes', __name__, static_folder='../static')

routes.add_url_rule('/api/schedule', view_func=schedule_create, methods=['PUT'])
routes.add_url_rule('/api/list', view_func=jobs_list, methods=['GET'])


routes.add_url_rule('/admin/drop', view_func=drop_collection, methods=['GET'])
