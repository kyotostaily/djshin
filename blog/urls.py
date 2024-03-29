from django.urls import path
from . import views

urlpatterns = [
    path('search/<str:q>/', views.PostSearch.as_view()), #598. views.py의 PostSearch에 대한 경로를 지정한다. 이제 views.py의 178째줄로 이동한다. (<str:q>는 검색어에 해당하는 값을 문자열(str)로 받고, 이 값을 q라고 부르겠다는 의미이다.)
    path('delete_comment/<int:pk>/', views.delete_comment), #577. views.py의 delete_comment에 대한 경로를 지정한다. 이제 views.py의 167째줄로 이동한다.
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()), #547. views.py의 CommentUpdate에 대한 경로를 지정한다. 이제 views.py의 156째줄로 이동한다.
    path('update_post/<int:pk>/', views.PostUpdate.as_view()), #384. tests.py의 239줄에 대한 경로를 지정한다. 그리고 views.py의 45째 줄로 이동한다.
    path('create_post/', views.PostCreate.as_view()), #334. PostCreate에 대한 경로를 지정하고 views.py의 28째 줄로 이동한다.
    path('tag/<str:slug>/', views.tag_page), #324. 이같이 입력하고 views.py의 47째 줄로 이동한다.
    path('category/<str:slug>/', views.category_page), #290. 변수명 slug를 받아온다. 이제 views.py의 맨 아래로 이동한다.
    path('<int:pk>/new_comment/', views.new_comment), #516. new_comment에 대한 처리에 대한 경로를 지정한다. 이제 views.py의 141째 줄로 이동한다.
    path('<int:pk>/', views.PostDetail.as_view()), #10. 자료형태가 int로 오고 /로 끝날때, views.py에 있는 single_post_page(포스트 하나만 구체적으로 보여주는 페이지)로 가라 라는 뜻 - blog/views.py로 간다. 45. single_post_page -> PostDetail.as_view()로 바꿔주고 46. single_page.html으로 이동하여 post_detail.html로 이름을 변경한다(모델명_detail형식). 이래야 views.py가 인식을 한다.
    path('', views.PostList.as_view()), #34. 아래 내용을 주석처리하거나 삭제 하고 입력 as_view는 약속의 의미로 보면 된다. 다시 views.py로 이동한다.
    #path('', views.index), #2. djshin_prj에 있는 urls.py에서 와서 봤는데 아무것도 없으면(''), views.py에 있는 index함수에 가서 봐라
]
