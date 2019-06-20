from django.urls import path

from . import views, commands

urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('login', views.LoginView.as_view(), name='login'),
    path('api', commands.Login.as_view(), name='login post')
]