# -*- coding: utf-8 -*-

from flask import Blueprint, current_app

from views.schedule import schedule_create

routes = Blueprint('routes', __name__, static_folder='../static')

routes.add_url_rule('/api/schedule', view_func=schedule_create, methods=['PUT'])
