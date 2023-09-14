import sys
def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return ["Hello, World! Deployed with SFTP"]