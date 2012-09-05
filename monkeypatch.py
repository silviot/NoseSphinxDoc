from webtest import TestApp

CHATS = []

class Recorder(object):

    def __init__(self):
        me = self
        self.do_request = TestApp.do_request
        self.chats = []

        def mydo_request(self, req, status, expect_errors):
            res = me.do_request(self, req, status, expect_errors)
            me.chats.append((req, res))
            return res

        TestApp.do_request = mydo_request

    def reset(self):
        self.chats = []