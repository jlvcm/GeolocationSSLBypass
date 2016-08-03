#!/usr/bin/env python
from bottle import route, run, template, request
from sys import argv

@route('/')
def index():
    return template('index.html', domain=request.headers.get('Referer', '*'))

if __name__ == "__main__":
    run(host='0.0.0.0', port=argv[1] if len(argv)>1 else 80)
