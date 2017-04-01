# -*- coding: utf-8 -*-
import app

class MessageHandling(object):


    def __init__(self, message_object):
        super(MessageHandling, self).__init__()
        self.message, self.address = message_object
        parse_message()


    def parse_message(self):
        app.logger.info(self.message)
