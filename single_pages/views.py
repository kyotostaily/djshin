from django.shortcuts import render
from blog.models import Post #639


def landing(request): #22. landing(대문페이지)함수입력
    recent_posts = Post.objects.order_by('-pk')[:3] #639. 역순으로 최근 3개까지 가져와라는 뜻이다. Post를 임포트한다.
    return render(
        request,
        'single_pages/landing.html', #23. templates파일 지정하고 single_pages/single_pages라는 폴더를 만들고 landing.html 파일을 만들고 이동한다.
        {
            'recent_posts': recent_posts, #640. 6째줄에서 설정한 recent_posts는 대문페이지의 recent_posts라고 연결시킨다. 그러면 landing.html에서 for문으로 반복해주면 된다. 이제 landing.html의 25째줄로 간다.
        }
    )


def about_me(request): #27. about_me에 대한 함수입력
    return render(
        request,
        'single_pages/about_me.html', #28. templates파일 지정하고 single_pages/single_pages/about_me.html을 만들고 그곳으로 이동한다.
    )
