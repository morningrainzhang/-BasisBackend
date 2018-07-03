# -*- coding: utf-8 -*-

import re
from six.moves import http_client
from six.moves import urllib
from wsgiref.headers import Headers


class Request(object):
    def __init__(self, environ):
        self.environ = environ

    @property
    def path(self):
        return self.environ['PATH_INFO']

    @property
    def args(self):
        """ 把查询参数转成字典形式 """
        get_arguments = urllib.parse.parse_qs(self.environ['QUERY_STRING'])
        return {k: v[0] for k, v in get_arguments.items()}


class Response(object):
    def __init__(self, response=None, status=200, charset='utf-8', content_type='text/html'):
        self.response = [] if response is None else response
        self.charset = charset
        self.headers = Headers([])
        content_type = '{content_type}; charset={charset}'.format(content_type=content_type, charset=charset)
        self.headers.add_header('content-type', content_type)
        self._status = status

    @property
    def status(self):
        status_string = http_client.responses.get(self._status, 'UNKNOWN')
        return '{status} {status_string}'.format(status=self._status, status_string=status_string)

    def __iter__(self):
        for val in self.response:
            if isinstance(val, bytes):
                yield val
            else:
                yield val.encode(self.charset)


# 试试结合了 Resquest 和 Response 的新 application:
def request_response_application(func):
    def application(environ, start_response):
        request = Request(environ)
        response = func(request)
        start_response(
            response.status,
            response.headers.items()
        )
        return iter(response)
    return application


class NotFoundError(Exception):
    """ url pattern not found """
    pass


class DecoratorRouter:
    def __init__(self):
        self.routing_table = []    # 保存 url pattern 和 可调用对象

    def match(self, path):
        for (pattern, callback) in self.routing_table:
            m = re.match(pattern, path)
            if m:
                return (callback, m.groups())
        raise NotFoundError()

    def __call__(self, pattern):
        def _(func):
            self.routing_table.append((pattern, func))
        return _


routers = DecoratorRouter()


@routers(r'/hello/(.*)/$')
def hello(request, name):
    return Response("<h1>Hello, {name}</h1>".format(name=name))


@routers(r'/goodbye/(.*)/$')
def goodbye(request, name):
    return Response("<h1>Goodbye, {name}</h1>".format(name=name))


def application(environ, start_response):
    try:
        request = Request(environ)
        callback, args = routers.match(request.path)
        response = callback(request, *args)
    except NotFoundError:
        response = Response("<h1>Not found</h1>", status=404)
    start_response(response.status, response.headers.items())
    return iter(response)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('127.0.0.1', 8000, application)
    httpd.serve_forever()
