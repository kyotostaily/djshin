from django.shortcuts import render
from .models import Post #5. Post 라는 것이 blog/models.py에 정의되어 있으므로 임포트한다.


def index(request): # 함수에는 항상 request가 온다고 생각해라.
    posts = Post.objects.all().order_by('-pk') #6. Post를 임포트 한 후 입력 (이렇게 하면 모든 포스트를 다 가져온다는 뜻)
                                               #9. order_by('-pk')를 하면 역순(최신순)으로 보여준다. pk는 그 반대.
    return render(
        request,
        'blog/index.html', #3. blog안에 있는 index.html을 랜더링 해라 라는 뜻이다.(blog/templates/blog/index.html을 만든다)
        {
            'posts': posts, #7. 딕셔너리 형태로 'posts': posts의 형태로 입력하면 index.html에 가서 사용할 수 있다.('posts'란 이름 말고도 다른것 써도 된다.)
        }                   #7. 이렇게 입력 후 html.index로 간다.
    )                       #7. posts의 결과가 index.html에 담긴다.
