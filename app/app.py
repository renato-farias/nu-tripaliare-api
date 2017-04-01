#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import thread
import socket
import logging.config

from flask import Flask
from modules.clustering import Clustering
from modules.broadcaster import Broadcaster
from werkzeug.contrib.cache import SimpleCache
from modules.message_handling import MessageHandling


app = Flask('nu-tripaliare-api', static_url_path='')
app.secret_key = 'nu-tripaliare-api'

logging.config.dictConfig(yaml.load(open('config/logging.yaml')))
logger = app.logger

cache = SimpleCache()

cluster = Clustering()

def read_brd(thread_name):
    logger.debug('[Thread-%d] Loading Broadcaster' % thread_name)
    broadcaster = Broadcaster()
    broadcaster.start()
    broadcaster.send({
            'type': 'join_cluster',
            'node_name': socket.gethostname()
        })
    cluster.add_node(socket.gethostname())
    while True:
        MessageHandling(broadcaster.read())

thread_name = 1
logger.info('Starting new Thread [%d]' % thread_name)
thread.start_new_thread(read_brd,(thread_name,))



@app.route('/')
def hello_world():
    return str(cluster.get_nodes())


if __name__ == '__main__':
    try:
        app.run(debug=False)
    except Exception, e:
        import sys, traceback
        traceback.print_exc(file=sys.stdout)
        print str(e)
