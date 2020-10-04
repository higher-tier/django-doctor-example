from django.urls import path, re_path

from . import views

app_name = 'core-app-1'

urlpatterns = [
    re_path(r'^re-path/with-parameter/(?P<parameter>.+)/', views.View7.as_view(), name='view-e-re-path-parameter'),
    re_path(r'^re-path/with-parameter/(?P<parameter>.+)/subpath/', views.View8.as_view(), name='view-f-re-path-parameter'),
]
