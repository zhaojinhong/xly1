from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View


class CollectHostInfo(View):

    def get(self, request):
        pass

    def post(self, request):
        print(request.POST)
        return HttpResponse("succxxxxxxxxxxxxxx.")

