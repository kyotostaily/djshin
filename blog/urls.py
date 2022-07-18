from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #2. djshin_prj에 있는 urls.py에서 와서 봤는데 아무것도 없으면(''), views.py에 있는 index함수에 가서 봐라
]
