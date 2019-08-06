from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import View
from apps.users.models import UserProfile
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username_info = ''
        password_info = ''
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username is '':
            username_info = '用户名不能为空'
        if password is '':
            password_info = '密码不能为空'
        if username is '' or password is '':
            return render(request, 'login.html', {'username_info': username_info,
                                                  'password_info': password_info})
        # authenticate
        tag = authenticate(username=username, password=password)

        if tag:
            login(request, tag)
            return HttpResponseRedirect(reverse('index'))
        msg = '用户名密码错误'
        return render(request, 'login.html', {'msg': msg})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))


class IndexView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return render(request, 'index.html')

