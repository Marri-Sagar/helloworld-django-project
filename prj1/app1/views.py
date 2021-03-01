from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.generic import View
from app1.mixin import HttpresponseMixin

def basic(request):
    d={"eno":100,"ename":"sagar","esal":5000}
    print(type(d))
    v="empno:{}empname:{}empsal:{}".format(d['eno'],d['ename'],d['esal'])
    v1=json.dumps(d)
    print(type(v1))
    return JsonResponse(d)

class cbv(View):
    def get(self,request,*args,**kwargs):
        d={"eno":101,"ename":"sagar"}
        return JsonResponse(d,content_type='application/json')
    def post(self,request,*args,**kwargs):
        d1={"msg":"post method"}
        return JsonResponse(d1,content_type='application/json')


class cbv1(HttpresponseMixin,View):
    def get(self,request):
        jsndata =json.dumps({"msg":"concept based on mixin concept"})
        return self.render_to_httpresponse(jsndata)




