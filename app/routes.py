# -*- coding: utf-8 -*-

from flask import Blueprint, current_app

routes = Blueprint('routes', __name__, static_folder='../static')
