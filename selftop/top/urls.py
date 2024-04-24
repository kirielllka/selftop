from django.urls import path
from top.views import Topself
urlpatterns = [
    path('', Topself.index, name='top-index'),
    path('sign-up/', Topself.sign_up, name='top-signup'),
    path('log-in/', Topself.log_in, name='top-login'),
    path('log-out', Topself.log_out, name='top-logout'),
    path('toppage/', Topself.toppage, name='toppage'),
    path('<int:home_id>/', Topself.homework, name='homework-page')
]