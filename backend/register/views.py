from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models.user import registered_user

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def first_time_register(request):
    if request.method == "POST":
        data = request.POST
        user_name = data.get('user_name')
        IP_address = request.POST.get
        # item = registered_user(user_name = "testing_user_name222", IP_address= "testing_user_IP")
        # item.save()
        # return "string"
        return HttpResponse('user_name')
