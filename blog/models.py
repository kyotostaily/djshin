from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) #77. head_image(게시물 맨 위의 이미지)를 넣을수 있도록 이렇게 입력한다.blank=True의 의미는 공백을 검사하지 않는다는 것이다. 즉 여기서는 이미지가 있을수도 없을수도 있게 하는것이다. 78. 이후 cmder에서 pip install Pillow(파이썬에서 이미지를 다룰수 있게 하는 패키지)로 설치하고 79. python manage.py makemigrations를 실행하면서 데이터베이스에 변화가 있다는 것을 알려주고 80. python manage.py migrate를 입력해서 데이터에 반영을 한다. 81. 이후 서버를 열어서 admin에서 이미지 파일 게시글에 추가해서 세이브 하면서 테스트 해 본다. 그러면 _media폴더 안에 년월일 폴더가 생기면서 이미지 파일이 저장이 된다. 이제 djshin_prj의 urls.py로 이동한다.
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True) #87. 파일 업로드를 위해 이렇게 입력한 후 cmder에서 python manage.py makemigrations를 한 후 python manage.py migrate를 해서 반영하고 admin 들어가서 파일을 저장해보며 테스트한다.

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author: 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self): #19. index.html에서 지정하려한 함수를 정의한다.
        return f'/blog/{self.pk}/' #고유의 url정의.
