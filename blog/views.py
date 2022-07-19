from django.shortcuts import render
from django.views.generic import ListView #32. list를 보여주는 것은 ListView라는 것이 있다. 이것을 상속받아서 확장하면 된다.
from .models import Post #5. Post 라는 것이 blog/models.py에 정의되어 있으므로 임포트한다.

#39. ListView를 확장해서 model을 어떤 모델을 쓸것인지 정의하고(model = Post), ordering을 바꿔주면 된다. 그리고 파일명도 post_list.html로 바꿔준다.
class PostList(ListView): #38. 리스트를 보여주고 싶으면 이렇게 모델명만 적어주면 된다.
    model = Post #33. 여기까지 입력 후 blog/urls.py로 이동한다.
    ordering = '-pk' #37. 파일 이름을 post_list.html로 바꾸고 ordering을 지정해서 최신순으로 해 준다.
    # 35. 이 클래스에서 리스트 뷰로 넘길 때는 항상 모델명_리스트의 형태로 넘기게 되어있다. ex) template_name = 'blog/post_list.html' index.html로 이동한다.

#31. def index를 주석처리 한다.
#def index(request): # 함수에는 항상 request가 온다고 생각해라.
    #posts = Post.objects.all().order_by('-pk') #6. Post를 임포트 한 후 입력 (이렇게 하면 모든 포스트를 다 가져온다는 뜻)
                                               #9. order_by('-pk')를 하면 역순(최신순)으로 보여준다. pk는 그 반대.
    #return render(
        #request,
        #'blog/post_list.html', #3. blog안에 있는 index.html을 랜더링 해라 라는 뜻이다.(blog/templates/blog/index.html을 만든다)
        #{
            #'posts': posts, #7. 딕셔너리 형태로 'posts': posts의 형태로 입력하면 index.html에 가서 사용할 수 있다.('posts'란 이름 말고도 다른것 써도 된다.)
        #}                   #7. 이렇게 입력 후 html.index로 간다.
    #)                       #7. posts의 결과가 index.html에 담긴다.


def single_post_page(request, pk): #11. 이렇게 함수를 만들고, request와 앞서 blog/urls.py에서 추가 했던 인자 pk를 추가한다.
    post = Post.objects.get(pk=pk) #12. get(pk=pk) pk가 같은pk인것을 가져와라! pk는 id랑 똑같은 것이다. pk는 필드를 만들지 않아도 models.py에서 자동으로 django가 제공을 한다.

    return render( #13. render는 장고에서 제공하는 기능이다.
        request,
        'blog/single_page.html', #14. 16. 이렇게 입력하고 blog/templates/blog 안에 single_page.html을 만든다.
        {
            'post': post, #15. 7번의 방법대로 하면서 이름만 다르게 post = post 로 한다.
        }
    )