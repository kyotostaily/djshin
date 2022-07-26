from django.db import models
from django.contrib.auth.models import User #181. User의 사용을 위해 임포트 한다.
import os #95. 파일 이름을 가져오기 위해 import os 패키지를 입력한다.


class Post(models.Model):
    title = models.CharField(max_length=50)
    hook_text = models.CharField(max_length=100, blank=True) #108. hook_text(요약문:이름은 자기맘대로) 109.이제 cmder에서 migration(인식)과 migrate(반영)를 한다. 이제 templates파일 수정을 위해 post_list.html(95째줄)로 간다.
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) #77. head_image(게시물 맨 위의 이미지)를 넣을수 있도록 이렇게 입력한다.blank=True의 의미는 공백을 검사하지 않는다는 것이다. 즉 여기서는 이미지가 있을수도 없을수도 있게 하는것이다. 78. 이후 cmder에서 pip install Pillow(파이썬에서 이미지를 다룰수 있게 하는 패키지)로 설치하고 79. python manage.py makemigrations를 실행하면서 데이터베이스에 변화가 있다는 것을 알려주고 80. python manage.py migrate를 입력해서 데이터에 반영을 한다. 81. 이후 서버를 열어서 admin에서 이미지 파일 게시글에 추가해서 세이브 하면서 테스트 해 본다. 그러면 _media폴더 안에 년월일 폴더가 생기면서 이미지 파일이 저장이 된다. 이제 djshin_prj의 urls.py로 이동한다.
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True) #87. 파일 업로드를 위해 이렇게 입력한 후 cmder에서 python manage.py makemigrations를 한 후 python manage.py migrate를 해서 반영하고 admin 들어가서 파일을 저장해보며 테스트한다. 이후 blog/post_list.html로 이동한다.

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #181. 유저(작성자)가 탈퇴되면 글까지 같이 지워지는 기능 183.(User, on_delete=models.CASCADE) -> (User, null=True, on_delete=models.SET_NULL)로 바꾸고 makemigrations 후 migrate를 하면 작성자가 탈퇴해도 글은 남아있다. 이제 tests.py의 9째줄로 이동한다.

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}' #182. 이렇게 입력하고 makemigrations를 하고 선택지나오면(1번 후 1번)하고, migrate를 한다. 그러면 admin들어가보면 post란에 author(작성자) 선택란이 생겼다.

    def get_absolute_url(self): #19. index.html에서 지정하려한 함수를 정의한다.
        return f'/blog/{self.pk}/' #고유의 url정의.

    def get_file_name(self): #94. 확장자를 알려면 파일 이름을 알아야 하므로 file_name 입력하고(업로드 파일의 이름을 가져오는 함수),
        return os.path.basename(self.file_upload.name) #96. os.path(경로).basename(self.file_upload.name), post_detail로 이동한다.

    def get_file_ext(self): #99. 확장자만 가져오는 함수
        return self.get_file_name().split('.')[-1] #100. '.' 으로 스플릿을 해서 맨 마지막에 확장자[-1]를 가져온다. 그리고 post_detail로 이동한다.