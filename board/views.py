from django.shortcuts import redirect #709
from django.views.generic import ListView, DetailView, CreateView #677, 691.
from django.contrib.auth.mixins import LoginRequiredMixin #699.
from .models import Board #678.
from .forms import BoardForm #718.


class BoardList(ListView): #677. BoardList의 내용을 작성후 ListView를 임포트 해준다. (blog/views.py의 5째줄의 내용을 복사후 붙여넣고 UpdateView는 지운다.)
    model = Board #678.이와같이 입력후 Board도 임포트 한다. 이제 board/templates를 만들고 그안에 board를 만들고 그 안에 board_list.html을 만들고 이동한다.
    ordering = '-pk' #681. 게시판이 최신것이 위로 가도록 이와같이 입력한다. 이제board_list.html로 이동한다.


class BoardDetail(DetailView): #691. BoardDetail의 내용을 작성후 DetailView를 임포트 해준다.
    model = Board #692. 이렇게 작성 후 board_list.html의 18번째 줄로 간다.


class BoardCreate(LoginRequiredMixin, CreateView): #699. BoardCreate에 대한 내용을 이와같이 작성한다. LoginRequiredMixin은 로긴한 사람만 와야되니 붙여주고 임포트한다.
    model = Board
    form_class = BoardForm #718. form_class의 내용을 이같이 입력하고 BoardForm을 5째줄에 임포트한다. 이제 settings.py의 156째줄로 이동한다.

    def form_valid(self, form): #704. blog/views.py의 41~42의 내용을 복사해서 붙인다.
        current_user = self.request.user
        if current_user.is_authenticated: #705. 43줄의 내용을 가져와서 이와같이 바꿔준다.
            form.instance.author = current_user #706. 44줄의 내용을 가져와서 이와같이 바꿔준다.
            response = super(BoardCreate, self).form_valid(form) #707. 45줄의 내용을 가져와서 이와같이 바꿔준다.

            return response #708. 60,61,62의 내용을 붙인다.
        else:
            return redirect('/board/') #709. redirect를 임포트한다. #710. 이제 인터넷에서 django-summernote를 검색해서 들어가서 양식에 있는 순서를 따른다. pip install django-summernote -> 이제 settings.py의 50째줄로 이동한다.