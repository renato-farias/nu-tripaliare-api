# -*- coding: utf-8 -*-
import app
from ast import literal_eval

class MessageHandling(object):

    def __init__(self, message_object):
        super(MessageHandling, self).__init__()
        self.message, self.address = message_object
        self.parse_message()


    def str_to_dict(self):
        try:
            return literal_eval(self.message)
        except:
            return {'message': 'undefined message'}


    def parse_message(self):
        app.logger.debug('[%s] Message received: %s' % \
                    ('MessageHandling', self.message))
        msg = self.str_to_dict()

        if 'type' not in msg.keys():
            app.logger.debug('[%s] Message can not be parsed.: %s' % \
                            ('MessageHandling', 'Type is missing'))
            return

        if msg['type'] == 'ping_cluster':
            app.cluster.node_handler(msg['node_name'])

        if msg['type'] == 'leave_cluster':
            app.cluster.remove_node(msg['node_name'])


