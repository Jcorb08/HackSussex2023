from django.shortcuts import render
from django.http import HttpResponse
from .models.user import registered_user
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



def first_time_register(request):
    item = registered_user(user_name = "testing_user_name", IP_address= "testing_user_IP")
    item.save()
    return HttpResponse("succefully register")