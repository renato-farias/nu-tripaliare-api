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


    def get_timeout_node(self, last_ping):
        return int(last_ping)+30


    def update_last_ping(self, node):
        for n in self.nodes:
            if n['node'] == node:
                n['last_ping'] = self.get_current_time()
                break
        return


    def node_handler(self, node):
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
        self.node_handler(os.environ['APP_HOST'])
        app.broadcaster.send({
                'type': 'ping_cluster',
                'node_name': os.environ['APP_HOST']
            })


    def leave(self):
        app.broadcaster.send({
                'type': 'leave_cluster',
                'node_name': os.environ['APP_HOST']
            })


    def remove_node(self, node):
        for n in self.nodes:
            if n['node'] == node:
                self.nodes.remove(n)


    def get_nodes(self):
        return self.nodes


    def remove_down_nodes(self):
        for n in self.nodes:
            if self.get_timeout_node(n['last_ping']) > self.get_current_time:
                app.logger.debug('[%s] Removing node from cluster: (%s)' % \
                                                ('Clustering', n['node']))
                self.nodes.remove(n)

