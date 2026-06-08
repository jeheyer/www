#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def application(environ, start_response):
    headers = [('Content-type', 'text/plain')]
    try:
        code = "200 OK"
        output = str({k:v for k,v in os.environ.items()})
    except Exception as e:
        code = "500 Internal Server Error"
        output = str(format(e))
    start_response(code, headers)
    return [output.encode('utf-8')]
