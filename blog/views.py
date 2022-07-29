from django.shortcuts import render
from django.views.generic import ListView, DetailView #32. list를 보여주는 것은 ListView라는 것이 있다. 이것을 상속받아서 확장하면 된다. 40. DeatailView는 하나만 보여주고 싶을 때 사용한다.(Post.objects.get)을 대체할 수 있다.
from .models import Post, Category #265. Category를 임포트 시킨다.

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