from django.shortcuts import render
from django.views.generic import ListView, DetailView #32. list를 보여주는 것은 ListView라는 것이 있다. 이것을 상속받아서 확장하면 된다. 40. DeatailView는 하나만 보여주고 싶을 때 사용한다.(Post.objects.get)을 대체할 수 있다.
from .models import Post, Category, Tag #265. Category를 임포트 시킨다. 325.Tag임포트.

#39. ListView를 확장해서 model을 어떤 모델을 쓸것인지 정의하고(model = Post), ordering을 바꿔주면 된다. 그리고 파일명도 post_list.html로 바꿔준다.
class PostList(ListView): #38. 리스트를 보여주고 싶으면 이렇게 모델명만 적어주면 된다.
    model = Post #33. 여기까지 입력 후 blog/urls.py로 이동한다.
    ordering = '-pk' #37. 파일 이름을 post_list.html로 바꾸고 ordering을 지정해서 최신순으로 해 준다.
    # 35. 이 클래스에서 리스트 뷰로 넘길 때는 항상 모델명_리스트의 형태로 넘기게 되어있다. ex) template_name = 'blog/post_list.html' index.html로 이동한다.

    def get_context_data(self, **kwargs): #263. 이렇게 하면 위의 ListView가 제공하는 것은 그대로 다 쓰면서 다른 내용을 추가할 수 있다.
        context = super(PostList, self).get_context_data() #263.
        context['categories'] = Category.objects.all() #264. base.html에 있는 categories의 for문(40~44)을 돌리기 위해서 입력한다.
        context['no_category_post_count'] = Post.objects.filter(category=None).count() #265. 미분류인 것들(카테고리가 없는것들category=None)이 몇개인지count()를 알려주기 위해서 입력한다.
        return context #266. 끝에는 이렇게 처리한다. 이제 base.html의 41~43으로 간다.


class PostDetail(DetailView): #43. 이렇게 써놓고 확장한다.
    model = Post

    def get_context_data(self, **kwargs): #276. 위엣것을 복사해서 이와같이 바꿔준다. 이제 post_list.html의 18~22을 복사해서 post_detail.html의 9번째 줄에 붙여주고 그곳으로 이동한다.
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


def category_page(request, slug): #291. category_page의 함수를 아래와같이 작성한다.
    if slug == 'no_category': #292. 미분류일때
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else: #293. 아니면 slug로 넘어오는 것이 있을때 slug와 똑같은 것을 가져오라는 뜻이다.
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category
        }
    )#294. 여기서는 클래스뷰가 아니기 떄문에 기본적으로 이와같이 다 설정을 해 주어야 한다. 위의 13,14줄의 내용을 참고하여 똑같이 써 준다. 이제 post_list.html으로 이동한다.


def tag_page(request, slug): #325. tag_page에 대한 함수를 바로위에서 복사하여 붙여넣고 아래와 같이 입력하고(48~61) 위에 Tag를 임포트 한다. 이제 post_list.html의 9째줄로 이동한다.
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all() #이렇게 입력해야 post_list에 내용을 다 넘길수 있다.

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'tag': tag
        }
    )