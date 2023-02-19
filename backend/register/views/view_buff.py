from django.http import HttpResponse, JsonResponse
from ..models.buff import standard_buff
import json


def initial_standard_buff_table(request):
    if request.method == "GET":
        with open('../static/SBT.json') as f:
            data = json.loads(f.read())

        # reset and create again
        standard_buff.objects.all().delete()
        for buff in data.keys():
            item = data[buff]
            insert_buff = standard_buff(buff_name = buff, attack = item['Attack'], deffence = item['Defence'], speed = item['Speed'])
            insert_buff.save()
            
        return HttpResponse("success initial standard_buff_table")

def get_all_standard_buffs(request):
    if request.method == "GET":

        data = {}
        for ob in standard_buff.objects.all():
            data[ob.buff_name] = ob.attack
        return JsonResponse(data)