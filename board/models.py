from django.db import models
from django.contrib.auth.models import User


class Board(models.Model): #666. Board에 대한 함수를 이것(1~18)과 같이 입력한다.
    title = models.CharField(max_length=150) #667. 제목
    content = models.TextField() #668. 콘텐츠

    created_at = models.DateTimeField(auto_now_add=True) #669. 작성일
    updated_at = models.DateTimeField(auto_now=True) #670. 수정일

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #671. 작성자. 이렇게 작성후 settings.py의 53째줄로 이동한다.

    def __str__(self): #674. blog/models.py의 49~50의 내용을 붙여넣는다.(프라이머리키(pk), 타이틀, 작성자의 입력창. djshin.prj/urls.py의 24째줄로 이동한다.
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self): #688. blog/models.py의 52~53의 내용을 붙여넣고
        return f'/board/{self.pk}/' #689. 이렇게 board로 바꿔준다. 이렇게 하면 pk의 번호에 맞게 이동할수 있다. 이제 board/urls.py의 6째줄로 이동한다.