from django.core.exceptions import PermissionDenied #390.PermissionDenied를 임포트 한다.
from django.shortcuts import render, redirect #365. redirect를 임포트한다.
from django.views.generic import ListView, DetailView, CreateView, UpdateView #335. CreateView를 임포트한다. 385.UpdateView임포트
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #373., UserPassesTestMixin임포트
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


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView): #373. LoginRequiredMixin은 로그인될때만 페이지 열리게 하는 기능이며, UserPassesTestMixin(어떤 특수한 사용자만 들어오게 하고싶은 기능)를 추가하고 3째줄에 임포트한다.
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category'] #336. models.py의 Post에 가서 fields(사용할 필드들)안에 무엇이 있으면 좋겠는가 보고 입력해 넣는다. 337. 이제 blog/post_form.html을 만든다.

    def test_func(self): #374.UserPassesTestMixin을 할 때 이 테스트를 거치게 된다.
        return self.request.user.is_superuser or self.request.user.is_staff #375. superuser이거나 staff 일 때 이 페이지가 열려야 한다는 조건이다.

    def form_valid(self, form): #360. CreateView는 form_valid(form의 내용들이 유효한지 검사해주는 기능)라는 기능을 갖고있다. 이를 이용하여(오버라이딩) 아래와 같이(33~39) 입력한다.
        current_user = self.request.user #361. request한 사용자가
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):#362. 로그인을 했으면 #376. 로그인 되있는지 확인하고, current_user가 staff인지 superuser인지 확인. 이제 post_list.html의 4째줄로 이동한다.
            form.instance.author = current_user #363. PostCreate에서 만들어진 CreateView가 제공하는 폼에 instance에 채워진 author라는 필드를 currunt_user로 채워라는 뜻
            return super(PostCreate, self).form_valid(form) #364. 이와 같이 입력하여 원래 받아야 할 기능들은 다 받으면서 363까지의 form을 원래 기본설정으로 보내는 문장.
        else:
            return redirect('/blog/') #365. 로그인을 안했으면 redirect를 사용하여 /blog/로 돌려보낸다. 1째줄에 임포트한다. 이제 tests.py의 18째 줄로 이동한다.


class PostUpdate(LoginRequiredMixin, UpdateView): #385.PostUpdate에 대한 내용을 이와 같이(46~55) 입력하고 UpdateView와 ermissionDenied를 위에 임포트한다.
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category'] #386. 위의 fields와 같이 해준다.
    template_name = 'blog/post_update_form.html' #394. PostUpdate를 사용하기 위한 템플릿을 이와같이 따로 지정할 수 있다. 이제 post_update_form.html로 이동한다.

    def dispatch(self, request, *args, **kwargs): #387. 서버에 사용자가 요청할때 dispatch는 get방식으로 요청하는지 post방식으로 요청하는지를 구분해 주는 역할을 한다.
        if request.user.is_authenticated and request.user == self.get_object().author: #388.해당하는 포스트의 권한이 있는 유저인지 확인, UpdateView라는 것은 어떤 특정 db의 레코드(db에서 불러온 인스턴스)에 대해서 수정을 하려할때 사용하는 것인데, 이럴때 하나를 가져오는데, 그 하나를 가져올때, UpdateView에서 get_object()라는 함수를 제공하고 있다. 이때 블로그의 post요소가 하나 가져와 지면, views.py의 'update_post/<int:pk>/'에 따라 pk로 가져와 지는데, 이것을 UpdateView에서 알아서 처리해서 get_object()라는 함수에서 해당하는 pk(여기서는 tests.py의 post_003)에 대한 것을 가져와서 그 안에서 author(models.py에 정의되어 있는)를 가리키면서 지금 로그인 한 사람과 똑같은지 확인한다.
            return super(PostUpdate, self).dispatch(request, *args, **kwargs) #389. 맞으면 본래 dispatch의 역할을 하도록 이와같이 입력한다.
        else:
            raise PermissionDenied #390. 아니면 허가 거부(임포트), tests.py의 256으로 간다.


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