from django.shortcuts import render
from apps.users.models import UserProfile
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class UserMangerView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def get(self, request):
        username = request.GET.get('keyword', '')
        # test = UserProfile.objects.filter(username='liyongli',)
        # filter 结果 < QuerySet[ < UserProfile: liyongli >] >
        # print(test)
        if username:
            user_info = UserProfile.objects.all().values('username', 'name_cn', 'email', 'phone').filter(username=username)
        else:
            user_info = UserProfile.objects.all().values('username', 'name_cn', 'email', 'phone')

        return render(request, 'list.html', {'user_info': user_info})