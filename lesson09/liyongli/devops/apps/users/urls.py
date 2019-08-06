# -*- coding:utf-8 -*-
# author: lyl
from django.conf.urls import url
from apps.users.views import UserMangerView

urlpatterns = [
    url(r'^user_list/$', UserMangerView.as_view(), name='user_list'),

]