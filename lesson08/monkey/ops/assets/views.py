from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

from django.contrib.auth.models import User
from .models import Assets


class CollectHostInfo(View):

    def get(self, request):
        pass

    def post(self, request):
        import random
        data = request.POST.dict()
        data['hostname'] += str(random.randint(1, 100))
        data['mac_address'] = "{} {}".format(str(random.randint(1, 100)), str(random.randint(1, 100)))
        try:
            Assets.objects.create(**data)
        except Exception as e:
            print(e)
        return HttpResponse("succ.")



def AssetsView(request, *args, **kwargs):
    print(request)
    print("args: {}".format(args))
    print("kwargs : {}".format(kwargs))
    return HttpResponse("succ")
