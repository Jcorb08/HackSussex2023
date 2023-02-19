from django.http import HttpResponse
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



def initial_standard_equipments_table(request):
    pass