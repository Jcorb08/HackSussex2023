from django.http import HttpResponse
from ..models.registered_user import registered_user
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the register index.")

@csrf_exempt
def first_time_register(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        IP_address = request.META["REMOTE_ADDR"]
        return HttpResponse(request.POST['user_name'])
        # if registered_user.objects.filter(user_name = user_name).first() == None:
            
        #     item = registered_user(user_name = user_name, IP_address= IP_address)
        #     item.save()
        #     print("user name registered :", user_name)
        #     item = registered_user.objects.filter(user_name = user_name).first()

        #     return HttpResponse(str(item.pk))

        # else:
        #     return HttpResponse("succesful inserted user had been")

def reset_registered_user(request):
    if request.method == "GET":
        registered_user.objects.all().delete()
        return HttpResponse("succesful deleted registered_user table")

# def initial_standard_buff_table(request):
#     if request.method == "GET":
#         with open('../static/SBT.json') as f:
#             data = json.loads(f.read())
        
#         for item in data.keys():
#             print(item)
#         return JsonResponse(data)
