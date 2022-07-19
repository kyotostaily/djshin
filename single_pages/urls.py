from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me), #26. about_me라는 함수를 이용하라는 것을 입력 후, single_pages/views.py로 이동한다.(아무것도 없다가 about_me가 있으면 이것을 실행시킨다는 의미도 있다.)
    path('', views.landing), #21. 아무것도 없을 때('') 대문페이지(landing page)를 보여주는 걸 만든다. 이후 views.py에 landing이라는 함수가 있어야 하니 single_pages/views.py로 이동한다.
]
