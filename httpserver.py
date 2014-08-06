#!/usr/bin/env python
#-*- coding: utf-8 -*-
import tornado.web
import tornado.httpserver
import tornado.httpclient
import tornado.options
import tornado.ioloop
from tornado.options import define,options

import os
import json
import urlparse
import logging
import datetime
import signal

defaultport=8868
res_total=0
starttime = datetime.datetime.now()


class helloworld(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self):
        global res_total

        request=json.loads(self.request.body)
        stra=request['stra']
        strb=request['strb']
        retstr=stra+","+strb
        ret_json={"ret":retstr}
        #print ret_json
        res_total+=1

        self.write(json.dumps(ret_json))
        self.finish()


if __name__ == "__main__":
    settings={"template_path": os.path.join(os.path.dirname(__file__), "template") ,
    "static_path": os.path.join(os.path.dirname(__file__), "static") ,
    "debug":False,
    "cookie_secret":"61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo="}
    define("port", default=defaultport, help="run on the given port", type=int)
    define("no_keep_alive", default=True, help="specify the connection type", type=bool)
    logging.basicConfig(level=logging.ERROR,
                    format='[%(levelname)s] [%(asctime)s] [%(filename)s-line:%(lineno)d] [%(funcName)s-%(threadName)s] %(message)s',
                    datefmt='%a,%Y-%m-%d %H:%M:%S',
                    filename="./log/httpserver.log",
                    filemode='a')

    tornado.options.parse_command_line()
    app=tornado.web.Application(handlers=[
    (r"/helloworld/",helloworld),
    ],**settings
    )
    HttpServer=tornado.httpserver.HTTPServer(app, no_keep_alive=options.no_keep_alive)
    HttpServer.listen(options.port)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        endtime = datetime.datetime.now()
        test_time=(endtime-starttime).seconds
        print test_time
        print res_total
        qps=float(res_total)/float(test_time)
        print qps
        logging.error(str(test_time))
        logging.error(str(res_total))
        logging.error(str(qps))
        tornado.ioloop.IOLoop.instance().stop()

