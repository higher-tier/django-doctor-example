from django.urls import path, re_path

from . import views

app_name = 'core-app-1'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    re_path(r'^re-path/without-parameter/', views.View5.as_view(), name='view-c-re-path'),
    re_path(r'^re-path/without-parameter/subpath/', views.View6.as_view(), name='view-d-re-path'),
]
