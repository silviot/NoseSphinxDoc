from webtest import TestApp

CHATS = []

class Recorder(object):

    def __init__(self):
        me = self
        self.do_request = TestApp.do_request
        self.chats = []

        def mydo_request(self, req, status, expect_errors):
            res = me.do_request(self, req, status, expect_errors)
            if 'dontlog_web_chats' not in req.environ or not req.environ['dontlog_web_chats']:
                me.chats.append((req, res))
            return res

        TestApp.do_request = mydo_request
        # Enable json indentation
        import simplejson
        dumps_original = simplejson.dumps
        def my_dumps(obj, *args, **kwargs):
            if 'indent' not in kwargs:
                kwargs['indent'] = 2
            return dumps_original(obj, *args, **kwargs)
        simplejson.dumps = my_dumps

    def reset(self):
        self.chats = []