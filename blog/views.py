from django.core.exceptions import PermissionDenied #390.PermissionDenied를 임포트 한다.
from django.shortcuts import render, redirect, get_object_or_404 #518. get_object_or_404임포트
from django.utils.text import slugify #421. slugify임포트
from django.views.generic import ListView, DetailView, CreateView, UpdateView #335. CreateView를 임포트한다. 385.UpdateView임포트
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #373., UserPassesTestMixin임포트
from .models import Post, Category, Tag, Comment #548. Comment임포트 .models의 .은 현재 폴더를 의미한다.
from .forms import CommentForm #515. CommentForm임포트

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
        context['comment_form'] = CommentForm #515. forms.py의 내용이 여기에 씌워지게 하는 내용(7째줄에 임포트 한다.) 이제 urls.py의 9째줄로 이동한다.
        return context


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView): #373. LoginRequiredMixin은 로그인될때만 페이지 열리게 하는 기능이며, UserPassesTestMixin(어떤 특수한 사용자만 들어오게 하고싶은 기능)를 추가하고 3째줄에 임포트한다.
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category'] #401. 'tags'를 추가한다. 이제 post_form.html의 12째 줄로 이동한다. #403. 402의 과정을 거쳤으면 'tags'라는 항목을 지운다. 그러면 new post안의 tags의 항목이 사라진다. 이제 tests.py의 225째 줄로 이동한다.

    def test_func(self): #374.UserPassesTestMixin을 할 때 이 테스트를 거치게 된다.
        return self.request.user.is_superuser or self.request.user.is_staff #375. superuser이거나 staff 일 때 이 페이지가 열려야 한다는 조건이다.

    def form_valid(self, form): #360. CreateView는 form_valid(form의 내용들이 유효한지 검사해주는 기능)라는 기능을 갖고있다. 이를 이용하여(오버라이딩) 아래와 같이(33~39) 입력한다.
        current_user = self.request.user #361. request한 사용자가
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):#362. 로그인을 했으면 #376. 로그인 되있는지 확인하고, current_user가 staff인지 superuser인지 확인. 이제 post_list.html의 4째줄로 이동한다.
            form.instance.author = current_user #363. PostCreate에서 만들어진 CreateView가 제공하는 폼에 instance에 채워진 author라는 필드를 currunt_user로 채워라는 뜻(current_user가 author를 만든 사람이다.)
            response = super(PostCreate, self).form_valid(form) #410 return을 response = 로 변경한다.

            tags_str = self.request.POST.get('tags_str') #412.서버에서 사람이 submit버튼을 누르면 POST방식으로 전달될거라는 뜻.(html form에 보면 method가 post로 되어있기 때문), 이렇게 POST라는 것을 받아서 그 안에 tags_str이라는게 있는데 그걸 가져와서 여기 담아보라는 의미이다.
            if tags_str: #413. tags_str이 있는 경우 이와같이(45~47) 입력
                tags_str = tags_str.strip() #414. strip을 입력함으로 앞 뒤 띄어쓰기에 대한 것을 없애준다.
                tags_str = tags_str.replace(',', ';') #415. 콤마(,)도 세미콜론(;)으로 바꿔주는 기능
                tags_list = tags_str.split(';') #416. 스플릿도 세미콜론으로 해주는 기능.

                for t in tags_list: #417. 만약 3개를 입력했으면 그것들이 리스트 형태로 들어오기 때문에 그것을 반영을 해 주기 위한 것. tags_list로 for문을 돌면서 아래와 같이(50~55) 돌게 한다.
                    t = t.strip() #418.strip을 입력함으로 앞 뒤 띄어쓰기에 대한 것을 없애준다.
                    tag, is_tag_created = Tag.objects.get_or_create(name=t) #419.get_or_create(name=t): 만약에 name이 t인 것이 있으면 그냥 가져오고, 없으면 그것을 이름이 t인 것으로 새로 만든다음 가져와라 라는 의미, 그래서 하나는 tag:(만들거나 혹은 원래 있었던 것의 결과) is_tag_created(새로만들어진건지 아니면 있던건지) 이렇게 두가지를 리턴한다. 새로 만든다면is_tag_created에 True가 올거고 기존의 것이면 False가 들어온다.
                    if is_tag_created: #420. 만약 만들어진 것이라면(원래 admin에서 slug가 자동으로 만들어 졌지만, 이 test에서는 자동으로 만든게 아니다.)
                        tag.slug = slugify(t, allow_unicode=True) #421. 여기서는 자동으로 만든 것이 아니므로, slug라는 태그(models.py의 22째줄에 있는 slug)를 채워줘야 한다. tag.slug는 slugify라는 함수(3째줄에 임포트한다.)가 있고, 여기에 t (admin처럼 slugify를 만들어 달라는 것) 와 allow_unicode=True(한글) 기능을 입력한다.
                        tag.save() #422. 태그를 저장
                    self.object.tags.add(tag) #423. for문을 돌때마다 새로 만들어진 tag가 추가된다.
            return response #411 이것을 입력하면 이전과 똑같아진다. 424.이렇게 된 결과를 response한다. 이제 tests.py의 273줄로 이동한다.
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

    def get_context_data(self, **kwargs): #432. get_context_data : 추가로 어떠한 데이터를 넘길 수가 있다.
        context = super(PostUpdate, self).get_context_data() #433. 기본적으로 UpdateView에서 제공하는 context_data기능을 사용하기 위해 이렇게 입력한다. 그래야 기존의 기능을 사용할수 있다.
        if self.object.tags.exists(): #434. 만약에 가져온 포스트에 태그가 있으면
            tags_str_list = list() #435. 리스트 형태로 만들고
            for t in self.object.tags.all(): #436. 포스트의 태그를 다 가져와서 (for 문을 돌려서 tags_str_list.append에 추가로 append를 한다.)
                tags_str_list.append(t.name) #437. t 즉 태그의 이름을 리스트에 하나씩 다 담는것이다.
            context['tags_str_default'] = '; '.join(tags_str_list) #438. context['tags_str_default'] : tags_str_default라는 인자를 추가하여, (문자열로 만들기 위해) 위의 리스트에 있는 태그들을 세미콜론 ';'으로 join한다. 그리고 이 추가된 tags_str_default 인자는 post_update_form.html 16째줄에서 받게된다.(이동)
        return context #439. 그리고 끝에는 이렇게 return context로 마무리한다.

    def form_valid(self, form): #440. UpdateView에서 제공하는 form_vaild 기능을 추가하기 위해서 아래와 같이 입력한다.
        response = super(PostUpdate, self).form_valid(form)
        self.object.tags.clear() #441. self.object(게시물)에 달려있는 태그를 다 없앤다(지우는게 아니라 태그와 포스트의 연결을 끊는다)는 의미이다.

        tags_str = self.request.POST.get('tags_str') #442. 위에것의 값을 가져와서
        if tags_str: #443. (46~56의 내용을 가져와서)그 값이 있으면 아래의 내용(88~99)을 적용시킨다.
            tags_str = tags_str.strip()
            tags_str = tags_str.replace(',', ';')
            tags_list = tags_str.split(';')

            for t in tags_list:
                t = t.strip()
                tag, is_tag_created = Tag.objects.get_or_create(name=t)
                if is_tag_created:
                    tag.slug = slugify(t, allow_unicode=True)
                    tag.save()
                self.object.tags.add(tag)
        return response #443. django-crispy-forms 사이트로 가서 pip install django-crispy-forms를 찾아서 인스톨(가상환경이 열린 상황에서)한다. #444. 이제 settings.py의42째 줄로 이동한다.


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


def new_comment(request, pk): #517. new_comment에 대한 함수를 입력한다.(141~155)
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk) #518. get_object_or_404(pk의 넘버가 존재하지 않을때 404에러를 던져준다.)를 임포트한다.

        if request.method == 'POST': #519. request.method가 POST인 경우에만
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid(): #520. 이런 형식(폼)이 잘 되어있는지 점검
                comment = comment_form.save(commit=False) #521. 일단 아직 여기서 저장하지 말고
                comment.post = post
                comment.author = request.user
                comment.save() #522. 위의 내용이 다 차면 저장한다.
                return redirect(comment.get_absolute_url()) #523. 저장했으니 그 위치가 뜬다.
        return redirect(post.get_absolute_url()) #524. POST가 아니거나 폼이 아닌경우에는 redirect. 이제 tests.py의 233줄로 이동한다.
    else:
        raise PermissionError

class CommentUpdate(LoginRequiredMixin, UpdateView): #548. CommentUpdate에 대한 내용을 이(156~164)와같이 입력한다. 로긴한 사람만 쓰도록 LoginRequiredMixin을 사용했고 UpdateView를 상속받아 사용했다.
    model = Comment #548. 6째 줄에 임포트한다.
    form_class = CommentForm #549. from_class는 froms.py의 CommentForm을 가져와서 사용한다.

    def dispatch(self, request, *args, **kwargs): #550. CommentUpdate를 원본으로 삼고있는것이 69줄의 dispatch이고, dispatch는 get방식인지 post방식인지 알아차리는 동시에, 이사람이 로그인 했는지, 작성자인지 확인해서 이 둘이 맞는경우에만 UpdateView에서 제공하는 dispatch기능을 활용하게 했고, 이에 맞지 않으면 PermissionDenied를 사용한다.
        if request.user.is_authenticated and request.user == self.get_object().author: #552. urls.py에서 물고 들어오는 pk를 이곳의 get_object()에서 어떤 comment를 갖고올것인지 다룬다. 이제 templates/blog/comment_form.html을 만들고 이동한다.
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs) #551. 69~73의 내용을 복사해서 붙여넣으면서 CommentUpdate로 수정한다.
        else:
            raise PermissionDenied