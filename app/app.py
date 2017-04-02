#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import time
import thread
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
broadcaster = Broadcaster()
cluster = Clustering()

def read_brd(thread_name):
    logger.debug('[Thread-%d] Loading Broadcaster' % thread_name)
    broadcaster.start()
    cluster.join()
    while True:
        logger.debug('[Thread-%d] Wating for broadcast massages' % \
                                                        thread_name)
        MessageHandling(broadcaster.read())


def ping_brd(thread_name):
    logger.debug('[Thread-%d] Loading Clustering Pinger' % thread_name)
    while True:
        time.sleep(10)
        logger.debug('[Thread-%d] Telling to cluster that I am alive' % \
                                                            thread_name)
        cluster.ping()

logger.info('Starting new Thread [%d]' % 1)
thread.start_new_thread(read_brd,(1,))

logger.info('Starting new Thread [%d]' % 2)
thread.start_new_thread(ping_brd,(2,))


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
