from django.http import HttpResponse, JsonResponse
from ..models.equipment import standard_equipment
from ..models.shark import shark
from django.views.decorators.csrf import csrf_exempt

def get_initial_shark(request):
    if request.method == "GET":
        shark.objects.all().delete()
        for i in range(5):
            insert_shark = shark(attack = 5, deffence = 5, speed = 5, hp = 100)
            insert_shark.save()

        data = {}
        for ob in shark.objects.all():
            data[ob.pk] = ob.hp
             
        return JsonResponse(data)

def get_shark_hp(request):
    if request.method == "GET":
        data = {}
        for ob in shark.objects.all():
            data[ob.pk] = ob.hp
             
        return JsonResponse(data)
        
        
    