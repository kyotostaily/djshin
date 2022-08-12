from django import forms #714. blog/forms.py의 2째줄 내용을 복사해 붙인다.
from django_summernote.widgets import SummernoteWidget
from .models import Board #715.


class BoardForm(forms.ModelForm): #713. django-summernote의 Form에서 이 양식을 복사해 와서 붙여넣기 하고 이와같이 변경한다.
    class Meta:
        model = Board #715. 모델은 board로 하고 임포트 한다.
        fields = ['title', 'content'] #716. 필드는 타이틀과 컨텐트만 쓴다.
        widgets = {
            'content': SummernoteWidget(), #717. content에만 summernote 위젯을 적용시키고 django-summernote사이트의 form에서 임포트 양식(from django_summernote.widgets import SummernoteWidget)을 가져와 2째줄에 붙여 임포트한다. 이제 board/views.py의 19째줄로 이동한다.
        }