from django.shortcuts import render
from django.views.generic import View


# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        msg = ''
        username_info = ''
        password_ino = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username is '':
            username_info = '用户名不能为空'
        if password is '':
            password_info = '密码不能为空'
        if username or password is '':
            return render(request, 'login.html', {'username_info': username_info, 'password_info': password_info})

        # 查库操作，暂时不写。。。。
        if username != 'admin' or password != '123456':
            msg = '用户名密码错误'
        return render(request, 'login.html', {'msg': msg})


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
