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
    path('admin/', admin.site.urls), #1. 관리자 페이지의 url로 가라(기본제공)
    path('', include('single_pages.urls')), #20. 아무것도 없을 때('')는 single_pages만 보여주는 것만 남겨놓고 blog.urls에 있는 것을 복사해서 single_pages에 붙여넣는다.
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #83. 이와같이 입력한다.그럼 이미지 저장된거 클릭하면 그림이 나온다. 이후에 blog/post_list.html로 이동한다.