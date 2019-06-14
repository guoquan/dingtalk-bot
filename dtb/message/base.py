import json


class Message(object):
    def __init__(self, msgtype: str):
        self.msgtype = msgtype

    def dump(self):
        return json.dumps(vars(self)).encode('utf-8')
