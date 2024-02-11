from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
# Create your views here.
def say_hello(request):
    return HttpResponse("<h1>Hello world</h1>")
def user_profile(request):
    profile = {"name":"Kossi ADANOU","email":"k@immoask.com","phone":"9087666555"}
    return JsonResponse(profile)
def filter_queries(request,query_id):
    data= {"id":query_id,"title":"How get id from URL","description":"9087666555","status":200}
    return JsonResponse(data)

class QueryView(View):
    queries=[
        {
            "id":1,
            "title":"How get id from URL",
            "description":"9087666555",
            "status":200
        },
        {
            "id":2,
            "title":"How get id from URL",
            "description":"9087666555",
            "status":200
        }
    ]
    def get(self,request):
        return JsonResponse({"result":self.queries})
    def post(self,request):
        return JsonResponse({"statut":"ok"})