#!/usr/bin/env python3

import json
import logging
import tornado.ioloop
import tornado.web

class DefaultHandler(tornado.web.RequestHandler):
    def get(self):
        raise tornado.web.HTTPError(
            status_code=404,
            reason="Not Found"
        )

    def write_error(self, status_code, exc_info=None, **kwargs):
        self.finish({"error": self._reason})

class HealthHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({"health": True})

    def write_error(self, status_code, exc_info=None, **kwargs):
        self.finish({"error": self._reason})

def start(port: int):
    web = tornado.web.Application([
        (r"/api/v1/health", HealthHandler),
    ], default_handler_class=DefaultHandler)

    web.listen(port)
    logging.info("Started HTTP Server on %d", int(port))

    tornado.ioloop.IOLoop.current().start()
