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
        print("ahdfh")
        user_name = request.POST.get('user_name')
        IP_address = request.META["REMOTE_ADDR"]
        item = registered_user(user_name = user_name, IP_address= IP_address)
        item.save()
        return HttpResponse(user_name)
