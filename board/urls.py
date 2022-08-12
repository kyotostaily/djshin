from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.BoardCreate.as_view()), #698. board/views.py의 BoardCreate와 연결되는 내용이다. 이제 board/views.py의 16쨰줄로 이동한다.
    path('<int:pk>/', views.BoardDetail.as_view()), #690. blog/urls.py의 13째줄의 내용을 복사해 붙여넣고 이름을 BoardDetail이라고 변경하고 board/views.py의 12째줄로 이동한다.
    path('', views.BoardList.as_view()), #676. board/views.py의 BoardList와 연결되는 내용이다. 이제 board/views.py로 이동한다.
]