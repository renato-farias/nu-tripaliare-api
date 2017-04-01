# -*- coding: utf-8 -*-

import app
import time
import socket

class Clustering(object):

    def __init__(self):
        super(Clustering, self).__init__()
        self.nodes = []


    def get_current_time(self):
        return int(time.time())


    def get_timeout_node(self):
        return self.get_current_time()+10


    def update_last_ping(self, node):
        for n in self.nodes:
            if n['node'] == node:
                n['last_ping'] = self.get_current_time()
                break
        return


    def add_node(self, node):
        already = False
        for n in self.nodes:
            if n['node'] == node:
                already = True

        if not already:
            self.nodes.append({
                    'node': node,
                    'last_ping': self.get_current_time()
                })
        else:
            self.update_last_ping(node)
        return


    def pong(self, node):
        if add_node in self.nodes:
            self.update_last_ping(node)
        self.remove_down_nodes()


    def ping(self):
        app.broadcaster.send({
                'type': 'ping_cluster',
                'node_name': socket.gethostname()
            })


    def get_nodes(self):
        return self.nodes


    def remove_down_nodes(self):
        for n in self.nodes:
            if int(n['last_ping']) > self.get_timeout_node():
                self.nodes.remove(n)

