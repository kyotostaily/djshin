from django.db import models
from django.contrib.auth.models import User #181. User의 사용을 위해 임포트 한다.
import os #95. 파일 이름을 가져오기 위해 import os 패키지를 입력한다.
from markdownx.utils import markdown #459.
from markdownx.models import MarkdownxField #457.
from datetime import timedelta #557.


class Category(models.Model): #194. 카테고리 항목에 대한 설정
    name = models.CharField(max_length=50, unique=True) #195. 카테고리에 대한 이름(길이, unique=True는 유일해야 한다는 의미)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True) #196. slug는 이해할 수 있는 글자로 구분한다는 것이며 그래서 뒤에 당연히 unique가 와야하며, allow_unicode=True는 한글사용이 가능하다는 것을 의미한다.)

    def __str__(self): #197. 이걸 해줘야 admin에서 구분이 가능하다.
        return self.name #197. 이걸 가지고 보여주겠다는 의미이다. 이제 29줄로 내려간다.

    def get_absolute_url(self): #289. 일단 blog로 시작을 해서 category다음에 self.slug(고유값)을 이용해서 url을 만들겠다는 뜻이다.
        return f'/blog/category/{self.slug}/' #289. 이제 blog/urls.py의 5째줄로 이동한다.

    class Meta: #204. Category를 복수형의 이름으로 바꿔줄때 이와같이 입력한다.
        verbose_name_plural = 'Categories' #204. 이렇게 입력하고 205. cmder에서 pip install django_extensions를 입력해 설치후, pip install ipython을 설치하고 settings.py 40째 줄로 넘어간다.


class Tag(models.Model):  #298. 6~14의 내용을 복사해서 붙여넣고 Tag라고 이름을 바꿔준다.(Tag라는 모델을 새로 만들었고 아래와 같이 네임과 슬러그가 있음)
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name #300. 문자형태는 name을 돌려주는 형태로 했음. 이제 44줄로 이동한다.

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/' #299. tag라고 이름을 바꿔준다.


class Post(models.Model):
    title = models.CharField(max_length=50)
    hook_text = models.CharField(max_length=100, blank=True) #108. hook_text(요약문:이름은 자기맘대로) 109.이제 cmder에서 migration(인식)과 migrate(반영)를 한다. 이제 templates파일 수정을 위해 post_list.html(95째줄)로 간다.
    content = MarkdownxField() #456. 마크다운 적용을 위해서 사이트를 참고하여 이와같이 변경하고 #457. 이것을 임포트하고 pip uninstall django -> pip install django==3.2로 다운그레이드 후 makemigrations를 하고 migrate를 한다. 이제 post_form.html의 19줄로 간다.

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) #77. head_image(게시물 맨 위의 이미지)를 넣을수 있도록 이렇게 입력한다.blank=True의 의미는 공백을 검사하지 않는다는 것이다. 즉 여기서는 이미지가 있을수도 없을수도 있게 하는것이다. 78. 이후 cmder에서 pip install Pillow(파이썬에서 이미지를 다룰수 있게 하는 패키지)로 설치하고 79. python manage.py makemigrations를 실행하면서 데이터베이스에 변화가 있다는 것을 알려주고 80. python manage.py migrate를 입력해서 데이터에 반영을 한다. 81. 이후 서버를 열어서 admin에서 이미지 파일 게시글에 추가해서 세이브 하면서 테스트 해 본다. 그러면 _media폴더 안에 년월일 폴더가 생기면서 이미지 파일이 저장이 된다. 이제 djshin_prj의 urls.py로 이동한다.
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True) #87. 파일 업로드를 위해 이렇게 입력한 후 cmder에서 python manage.py makemigrations를 한 후 python manage.py migrate를 해서 반영하고 admin 들어가서 파일을 저장해보며 테스트한다. 이후 blog/post_list.html로 이동한다.

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #181. 유저(작성자)가 탈퇴되면 글까지 같이 지워지는 기능 183.(User, on_delete=models.CASCADE) -> (User, null=True, on_delete=models.SET_NULL)로 바꾸고 makemigrations 후 migrate를 하면 작성자가 탈퇴해도 글은 남아있다. 이제 tests.py의 9째줄로 이동한다.
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL) #198. (카테고리, null=True(데이터베이스안에 있어야된다 혹은 없어야된다를 정의), (blank=True:필수사항이 들어갔는지 아닌지 검사해준다) on_delete=models.SET_NULL(작성자가 탈퇴해도 글은 남아있다.) 이후, makemigrations와 migrate를 한다. 이제 admin.py로 간다.
    tags = models.ManyToManyField(Tag, blank=True) #301. tag를 다대다 관계 ManyToMany 로 설정후 makemigrations 이후 migrate를 한다. 이제 admin의 11째 줄로 간다.

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}' #182. 이렇게 입력하고 makemigrations를 하고 선택지나오면(1번 후 1번)하고, migrate를 한다. 그러면 admin들어가보면 post란에 author(작성자) 선택란이 생겼다.

    def get_absolute_url(self): #19. index.html에서 지정하려한 함수를 정의한다.
        return f'/blog/{self.pk}/' #고유의 url정의.

    def get_file_name(self): #94. 확장자를 알려면 파일 이름을 알아야 하므로 file_name 입력하고(업로드 파일의 이름을 가져오는 함수),
        return os.path.basename(self.file_upload.name) #96. os.path(경로).basename(self.file_upload.name), post_detail로 이동한다.

    def get_file_ext(self): #99. 확장자만 가져오는 함수
        return self.get_file_name().split('.')[-1] #100. '.' 으로 스플릿을 해서 맨 마지막에 확장자[-1]를 가져온다. 그리고 post_detail로 이동한다.

    def get_content_markdown(self): #459. content를 마크다운 형식으로 바꿔주는 함수이며 임포트를 해준다. 이제 post_detail.html의 46째 줄로 간다.
        return markdown(self.content)


class Comment(models.Model): #481. 댓글에 관한 내용을 아래와 같이(64~75) 입력한다.
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #482. 어떤 포스트에 대한 댓글인가에 관한 내용(모델이름:Post, on_delete=models.CASCADE: 글이 지워지면 아래 댓글도 다 지워지는 설정)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #483. 작성자가 누구인지 (다대일 매칭), 마찬가지로 글이 삭제되면 댓글 작성자도 삭제되도록
    content = models.TextField() #484. 댓글을 달면 content라는 내용으로 담긴다. 위(Post)에는 마크다운을 썼지만 여기선 텍스트필드를 사용했다. 왜냐면 마크다운 허용하면 이것저것 화려하게 다 꾸미기 때문이다.
    created_at = models.DateTimeField(auto_now_add=True) #485. 작성일 (41~42의 내용 복사해 붙여서 이와같이 변경)
    updated_at = models.DateTimeField(auto_now=True) #486. 수정일, 즉 5개의 필드가 있는 모델이 만들어짐

    def __str__(self): #487. admin에서 어떻게 보이게 할 것인가에 대한 함수
        return f'{self.author}::{self.content}' #488. 작성자가 누구고 내용이 무엇인지 보여준다. 이제 makemigrations 이후 migrater를 한다. 이제 admin.py의 2째줄로 간다.

    def get_absolute_url(self): #497. 포스트로 이동해와서 self.pk에 따른 곳으로 이동한다. 이 내용은 post_detail.html의 95번째 줄의 내용을 보고 움직인다. 이제 tests.py의
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'

    def is_updated(self): #557. post_detail에서 지정한 is_updated의 함수를 지정하고 timedelta를 6째줄에 임포트한다.
        return self.updated_at - self.created_at > timedelta(seconds=1) #558. 업데이트시간 - 최초작성시간이 1초보다 크다 라는 뜻, 이제 tests.py의 285줄로 이동한다.

    def get_avatar_url(self): #608. 구글로 로그인 한 사람들의 아바타가 나올수 있도록 이와같이(81~85) 함수를 입력한다.
        if self.author.socialaccount_set.exists(): #609. django-allauth를 이용해 소셜 로그인을 할 경우
            return self.author.socialaccount_set.first().get_avatar_url() #610. 그 로그인 계정의 아바타 URL을 가져온다.
        else:
            return f'https://doitdjango.com/avatar/id/1164/79445086251f6541/svg/{self.author.email}' #611. doitdjango.com으로 가서 Avatar메뉴에서 google로 접속한 후 create a project -> 자신의 도메인 입력 -> id/부여받은 id/부여받은key/svg/에 따라 이곳에 이와같이 입력한다. 이제 post_detail.html의 101째 줄로 간다.