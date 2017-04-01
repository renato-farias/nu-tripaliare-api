# -*- coding: utf-8 -*-
import app
from ast import literal_eval

class MessageHandling(object):


    def __init__(self, message_object):
        super(MessageHandling, self).__init__()
        self.message, self.address = message_object
        self.parse_message()


    def str_to_dict(self):
        return literal_eval(self.message)


    def parse_message(self):
        app.logger.info(self.str_to_dict())
