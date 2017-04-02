# -*- coding: utf-8 -*-

import os
import app
import time

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
            app.logger.debug('[%s] Adding new node on cluster: (%s)' % \
                                                ('Clustering', node))
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
                'node_name': os.environ['APP_HOST']
            })


    def join(self):
        # this line below is necessary to assurance the will be
        # joined on the cluster, because the MessageHandling
        # can take a long time to start
        self.add_node(os.environ['APP_HOST'])
        app.broadcaster.send({
                'type': 'join_cluster',
                'node_name': os.environ['APP_HOST']
            })


    def get_nodes(self):
        return self.nodes


    def remove_down_nodes(self):
        for n in self.nodes:
            if int(n['last_ping']) > self.get_timeout_node():
                self.nodes.remove(n)

