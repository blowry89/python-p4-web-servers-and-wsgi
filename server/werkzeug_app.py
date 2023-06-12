#!/usr/bin/env python3

from werkzeug.wrappers import Request, Response

@Request.application #run any code inside of the function in the browser at the location we specify.
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple( #runs a server for a one-page application without complications
        hostname='localhost',
        port=5555, 
        application=application
    )