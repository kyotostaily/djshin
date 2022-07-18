from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author: 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self): #19. index.html에서 지정하려한 함수를 정의한다.
        return f'/blog/{self.pk}/' #고유의 url정의.
