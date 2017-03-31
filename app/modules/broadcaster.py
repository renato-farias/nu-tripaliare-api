# -*- coding: utf-8 -*-

import socket
import struct

class Broadcaster(object):

    def __init__(self, **args):
        super(Listener, self).__init__()
        set_config(**args)


    def _set_config(self, **args):
        configs = {
            addr: '224.0.0.1',
            bind: '0.0.0.0',
            port: 3000
        }
        self.addr = args.get('addr', default=configs['addr'])
        self.bind = args.get('bind', default=configs['bind'])
        self.port = args.get('port', default=configs['port'])


    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        membership = socket.inet_aton(self.addr) + socket.inet_aton(self.bind)

        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, membership)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.sock.bind((bind, port))


    def read(self):
        """it returns a tuple (message, address)"""
        return self.sock.recvfrom(255)


    def send(self, message):
        ttl = struct.pack('b', 1)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
        self.sock.sendto(message, (self.addr, self.port))
