from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_post_page), #10. 자료형태가 int로 오고 /로 끝날때, views.py에 있는 single_post_page(포스트 하나만 구체적으로 보여주는 페이지)로 가라 라는 뜻 - blog/views.py로 간다.
    path('', views.index), #2. djshin_prj에 있는 urls.py에서 와서 봤는데 아무것도 없으면(''), views.py에 있는 index함수에 가서 봐라
]
