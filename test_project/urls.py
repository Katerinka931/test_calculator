from django.urls import path, re_path

from test_project.views import MainClass

urlpatterns = [
    re_path(r'^calculate$', MainClass.as_view(), name='main-page'),

]