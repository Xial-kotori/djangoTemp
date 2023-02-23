import json
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods as methods
from temp.models import Person


@methods(["GET"])
def index(req):
    return JsonResponse({
        "code": 0,
        "msg": "success"
    })


@methods(["POST"])
@csrf_exempt
def add_person(req: HttpRequest):
    data = json.loads(req.body)

    if not all(k in data.keys() for k in ["name", "gender", "age"]):
        return JsonResponse({
            "code": "1",
            "msg": "参数不全啊"
        })
    Person.objects.create(**data)
    return JsonResponse({
        "code": "0",
        "msg": "success"
    })
