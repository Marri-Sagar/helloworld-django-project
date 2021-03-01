from django.http import HttpResponse

class HttpresponseMixin(object):
    def render_to_httpresponse(self,jsndata):
        return HttpResponse(jsndata,content_type='application/json')
