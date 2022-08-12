"""djshin_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings #82. 이같이 입력한다.
from django.conf.urls.static import static #82. 이같이 입력해서 static까지 추가시킨다.

urlpatterns = [
    path('blog/', include('blog.urls')), #2. blog.urls에 가서 처리를 해라
    path('board/', include('board.urls')), #675. board.urls에 가서 처리를 하라는 뜻. 이제 blog/urls.py를 복사해서 board에 붙여넣는다. 그리고 board/urls.py로 이동한다.
    path('admin/', admin.site.urls), #1. 관리자 페이지의 url로 가라(기본제공)
    path('markdownx/', include('markdownx.urls')), #455. Markdownx사이트에서 urls.py의 내용을 찾아서 이와같이 복사해서 붙여넣는다. 그리고 이 내용 아래의 Next를 누르면서 다음 페이지로 넘어간다. 이제 models.py의 36째 줄로 넘어간다.
    path('accounts/', include('allauth.urls')), #470. django-allauth에서 복사하여 붙이고 migrate를 한다. 이후 #471. 사이트의 providers로 가서 google을 선택한 후, https://console.developers.google.com/에 들어간다(구글로긴필요). #472. 새 프로젝트 선택 -> 프로젝트 이름 설정 -> 만들기 -> 만들어진 프로젝트에 들어가서 -> Oauth동의화면 -> 외부 클릭 -> 만들기 -> 앱 이름, 사용자지원이메일, 개발자연락처정보 입력(여기선 djshinkyoto@gmail.com) -> 저장 후 계속 -> 사용자 인증 정보 -> Create credentials(사용자 인증 정보 만들기)클릭 -> OAuth클라이언트ID 클릭 -> 애플리케이션 유형 -> 웹 애플리케이션, 이름입력 -> 승인된 자바스크립트 원본 아래 url추가 : http://127.0.0.1:8000 입력 -> 승인된 리디렉션 url -> http://127.0.0.1:8000/accounts/google/login/callback/ 입력 -> 만들기 -> 클라이언트ID및 클라이언트 보안 비밀번호 따로 복사해서 보관 -> admin페이지의 sites에 간다. -> example.com클릭해서 Domain name과 Display name을 127.0.0.1:8000로 바꿔주고 save. 이제 navbar.html의 첫째줄로 이동한다.
    path('summernote/', include('django_summernote.urls')), #712. django-summernote메뉴얼의 순서에 따라 붙이고 migrate를 한다. 이제 board에 forms.py를 만들고 이동한다.
    path('', include('single_pages.urls')), #20. 아무것도 없을 때('')는 single_pages만 보여주는 것만 남겨놓고 blog.urls에 있는 것을 복사해서 single_pages에 붙여넣는다.
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #83. 이와같이 입력한다.그럼 이미지 저장된거 클릭하면 그림이 나온다. 이후에 blog/post_list.html로 이동한다.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)