from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models.registered_user import registered_user

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the register index.")


@csrf_exempt
def first_time_register(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        IP_address = request.META["REMOTE_ADDR"]

        if registered_user.objects.filter(user_name = user_name).first() == None:
            
            item = registered_user(user_name = user_name, IP_address= IP_address)
            item.save()
            print("insert user :", user_name)

            return HttpResponse(item.id)

        else:
            return HttpResponse("user had been inserted")
