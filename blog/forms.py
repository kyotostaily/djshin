from .models import Comment #513. 이와같이 형식을 작성한다.
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',) #514. content라는 필드를 쓰겠다는 뜻. 이제 views.py의 28째 줄로 이동한다.