from django.http import HttpResponse
from ..models.equipment import standard_equipment
import json


def initial_standard_equipments_table(request):
    if request.method == "GET":
        with open('../static/SET.json') as f:
            data = json.loads(f.read())

        # reset and create again
        standard_equipment.objects.all().delete()
        for equi in data.keys():
            item = data[equi]
            insert_equi = standard_equipment(equipment_name = equi, attack = item['Attack'], deffence = item['Defence'], speed = item['Speed'])
            insert_equi.save()
            
        return HttpResponse("success initial standard_equipment_table")


def get_all_standard_equipments(request):
    if request.method == "GET":
        return HttpResponse(standard_equipment.objects.all())