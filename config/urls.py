from django.urls import path, re_path, include
from django.views.generic import View


class View1(View):
    pass


class View2(View):
    pass


class View3(View):
    pass


class View4(View):
    pass



urlpatterns = [
    path('sub0/', include('example.aardvark.urls')),
    path('sub1/', include('example.rooster.urls', namespace='core-namespace-1')),
    path('path/without-parameter/', View1.as_view(), name='view-a-path'),
    path('path/without-parameter/subpath/', View2.as_view(), name='view-b-path'),
    path('path/with-parameter/<int:parameter>/', View3.as_view(), name='view-a-path'),
    path('path/with-parameter/<int:parameter>/subpath/', View4.as_view(), name='view-b-path'),
]
