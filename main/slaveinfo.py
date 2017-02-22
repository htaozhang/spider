#coding: utf-8

import json

class SlaveInfo:
    def __init__(self):
        self.id = None
        self.name = None
        self.self_ip = None
        self.path = None
        pass

    def __str__(self):
        return json.dumps(self.__dict__)

