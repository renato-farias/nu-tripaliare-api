#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import thread
import logging.config

from flask import Flask
from modules.broadcaster import Broadcaster
from modules.message_handling import MessageHandling
from werkzeug.contrib.cache import SimpleCache

app = Flask('nu-tripaliare-api', static_url_path='')
app.secret_key = 'nu-tripaliare-api'

logging.config.dictConfig(yaml.load(open('config/logging.yaml')))
logger = app.logger

cache = SimpleCache()

def read_brd(thread_name):
    logger.debug('[Thread-%d] Loading Broadcaster' % thread_name)
    broadcaster = Broadcaster()
    broadcaster.start()
    while True:
        MessageHandling(broadcaster.read())


@app.route('/')
def hello_world():
    return 'Hello, World!'


def app_run(thread_name):
    logger.debug('[Thread-%d] Loading App' % thread_name)
    try:
        app.run(debug=False)
    except Exception, e:
        import sys, traceback
        traceback.print_exc(file=sys.stdout)
        print str(e)


thread_name = 1
logger.info('Starting new Thread [%d]' % thread_name)
thread.start_new_thread(read_brd,(thread_name,))

thread_name = 2
logger.info('Starting new Thread [%d]' % thread_name)
thread.start_new_thread(app_run,(thread_name,))

