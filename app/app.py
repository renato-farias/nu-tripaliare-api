#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import time
import atexit
import thread
import logging.config

from flask import Flask
from routes import routes
from modules.clustering import Clustering
from modules.broadcaster import Broadcaster
from werkzeug.contrib.cache import SimpleCache
from modules.message_handling import MessageHandling

app = Flask('nu-tripaliare-api', static_url_path='')
app.secret_key = 'nu-tripaliare-api'

status = ['scheduled', 'queued', 'running', 'done', 'done_with_error']

logging.config.dictConfig(yaml.load(open('config/logging.yaml')))
logger = app.logger

cache = SimpleCache()
#broadcaster = Broadcaster()
#cluster = Clustering()

# def read_brd(thread_name):
#     logger.debug('[Thread-%d] Loading Broadcaster' % thread_name)
#     broadcaster.start()
#     cluster.join()
#     while True:
#         logger.debug('[Thread-%d] Wating for broadcast massages' % \
#                                                         thread_name)
#         MessageHandling(broadcaster.read())


# def ping_brd(thread_name):
#     logger.debug('[Thread-%d] Loading Clustering Pinger' % thread_name)
#     while True:
#         time.sleep(30)
#         logger.debug('[Thread-%d] Telling to cluster that I am alive' % \
#                                                             thread_name)
#         cluster.ping()


# def leave_cluster():
#     cluster.leave()


# def start_thread_read_brd():
#     logger.info('Starting new Thread [%d]' % 1)
#     thread.start_new_thread(read_brd,(1,))


# def start_thread_ping_brd():
#     logger.info('Starting new Thread [%d]' % 2)
#     thread.start_new_thread(ping_brd,(2,))


# start_thread_read_brd()
# start_thread_ping_brd()
# atexit.register(leave_cluster)


# @app.route('/')
# def hello_world():
#     return str(cluster.get_nodes())

## import routes
app.register_blueprint(routes)


if __name__ == '__main__':
    try:
        app.run(debug=False)
    except Exception, e:
        import sys, traceback
        traceback.print_exc(file=sys.stdout)
        print str(e)
