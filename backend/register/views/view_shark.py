from django.http import HttpResponse, JsonResponse
from ..models.equipment import standard_equipment
from ..models.shark import shark
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def post_for_attack_shark(request):
    if request.method == "POST":
        attack_value = standard_equipment.objects.filter(equipment_name = request.POST.get('equipment_name')).first().attack
        attacked_shark = shark.objects.filter(id = request.POST.get('shark_id')).first()
        attacked_shark.hp -= attack_value
        attacked_shark.save()
        
    return HttpResponse(attacked_shark.hp)



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
        
        
    