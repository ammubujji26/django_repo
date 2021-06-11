from django.http import HttpResponse

class Displaymiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("Request Before View Function call")
        response=self.get_response(request)
        print("Response from server")
        return response
    def process_exception(self,request,exception):
        return HttpResponse('<h1>Currently server has technical issue...so please wait for a minute</h1>')
class Custommiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print('custom request')
        response=self.get_response(request)
        print('custom response')
        return response
