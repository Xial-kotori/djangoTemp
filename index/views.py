from django.http import JsonResponse
from django.views.decorators.http import require_http_methods as methods


@methods(["GET"])
def index(request):
    return JsonResponse({
        "code": 0,
        "msg": "success",
        "data": "hello"
    })
