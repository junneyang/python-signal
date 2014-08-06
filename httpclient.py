#-*- coding: utf-8 -*-
#!/usr/bin/env python
import httplib
import json
import time

if __name__ == "__main__":
    ip_port="localhost:8868"
    params = ({
                "stra":"hello",
                "strb":"world"
    })
    url="/helloworld/"

    conn = httplib.HTTPConnection(ip_port)
    headers = {"Content-type":"application/json","Connection":"Keep-Alive"}
    #headers = {"Content-type":"application/json"}

    for i in xrange(2):
        conn.request("POST", url, json.JSONEncoder().encode(params), headers)
        response = conn.getresponse()
        data = response.read()
        print data
    conn.close()




