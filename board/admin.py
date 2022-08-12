from django.contrib import admin #673. admin에서 board를 생성해서 위해 이같이 입력한다. 이제 board/models.py의 14째줄로 이동한다.
from .models import Board

admin.site.register(Board)
