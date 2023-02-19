from django.http import HttpResponse
from ..models.registered_user import registered_user

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the register index.")

def first_time_register(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        IP_address = request.META["REMOTE_ADDR"]

        if registered_user.objects.filter(user_name = user_name).first() == None:
            
            item = registered_user(user_name = user_name, IP_address= IP_address)
            item.save()
            print("user name registered :", user_name)

            return HttpResponse(str(item.pk))

        else:
            return HttpResponse("user had been inserted")

def reset_registered_user(request):
    if request.method == "GET":
        registered_user.objects.all().delete()
        return HttpResponse("registered_user table had been deleted")

# def initial_standard_buff_table(request):
#     if request.method == "GET":
#         with open('../static/SBT.json') as f:
#             data = json.loads(f.read())
        
#         for item in data.keys():
#             print(item)
#         return JsonResponse(data)
