from django.http import HttpResponse, JsonResponse
from ..models.attack import attack_action
from django.views.decorators.csrf import csrf_exempt, csrf_protect


@csrf_exempt
def post_for_attack_shark(request):
    if request.method == "POST":
        action = attack_action(equipment=request.POST.get('equipment') , buff=request.POST.get('buff'), shark=request.POST.get('shark'))
        action.save()

        return HttpResponse('action had storged')

@csrf_exempt
def get_overall_attack(request):
    if request.method == "GET":
        data = []
        for ob in attack_action.objects.all():
            data.append({'shark' : ob.shark,'buff' : ob.buff,'equipment' : ob.equipment})
    
        
        # attack_action.objects.all().delete()
        response = HttpResponse(data)
        response.headers['Access-Control-Allow-Origin'] = '*'
    
        print(response)

        return response