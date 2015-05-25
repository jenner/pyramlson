from pyramid_raml import api_service, api_method

@api_service('/foo')
class ErrorsResource(object):

    def __init__(self, request):
        self.request = request

    @api_method('get')
    def get(self):
        raise Exception()

    @api_method('get', subpath='/{one}/{two}')
    def foo(self, one, two):
        return dict(one=one, two=two)
