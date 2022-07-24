from django.test import TestCase, Client #118. Client입력
from bs4 import BeautifulSoup #119.
from .models import Post #120. models도 가져와야 하기에 임포트한다.


class TestView(TestCase): #113. 이런식으로 TestCase를 확장시켜준다.
    def setUp(self): #116. setUp으로 시작한 후
        self.client = Client() #117. 이렇게 입력하고 위(from)에 TestCase옆에 Client(방문하려는 사람의 브라우저)를 입력한다.

    def test_post_list(self): #114. 여기서는, 함수를 시작할 때 test_post_list처럼 소문자로 시작한다. 이제 cmder에서 pip install beautifulsoup4(장고에서 웹개발, 파이썬 크롤링 할때 많이쓴다.)를 실행한다.
        # 1.1 포스트 목록 페이지(post list)를 연다. 테스트 할 것들을 이런식 으로 글을 쓰면서 준비를 한다.
        response = self.client.get('/blog/') #115. 서버에다 /blog/라는 url로 요청을 한다.(response)
        # 1.2 정상적으로 페이지가 로드된다.
        self.assertEqual(response.status_code, 200) #118. 200은 response(요청)한 것이 잘 로드되었다는 표시이다.
        # 1.3 페이지의 타이틀에 Blog라는 문구가 있다. 119. 이때 from bs4 import BeautifulSoup으로 임포트한다.
        soup = BeautifulSoup(response.content, 'html.parser') #121. beautifulsoup에서 콘텐츠를 가져오는 것을 response(요청)하는데 그게 html.parser(html형태)이다.
        self.assertIn('Blog', soup.title.text) #122. (바로 위에서 정의된 soup이 가져온) 페이지의 타이틀(title - html요소)의(.text)를 봤을때 Blog라는 문구가 안에 있어야 한다(self.assertIn) 라는 뜻이다.
        # 1.4 NavBar가 있다.
        navbar = soup.nav #123. soup.nav 즉, soup. 이후에 html 스크립트의 nav를 입력하면 nav로 접근하기 떄문이다.
        # 1.5 Blog, About me라는 문구가 Navbar에 있다.
        self.assertIn('Blog', navbar.text) #124. 122와 같은 방식으로 진행된다.
        self.assertIn('About me', navbar.text) #124. 122와 같은 방식으로 진행된다. 이제 python manage.py test를 해 본다.

        # 2.1 게시물이 하나도  없을 때
        self.assertEqual(Post.objects.count(), 0) #125. 게시물을 카운트 해 봤을때 0개와 같은(self.assertEqual)지 확인한다.
        # 2.2 메인 영역에 "아직 게시물이 없습니다" 라는 문구가 나온다.
        main_area = soup.find('div', id='main-area') #127. id 가 main-area라는 것을 가진 div를 찾아라는 뜻이고 그게 main_area이다.
        self.assertIn('아직 게시물이 없습니다', main_area.text) #126. 125의 내용이 확인될 때 이 내용('아직 게시물이 없습니다')이 메인영역(main_area.text) 안에 있어야 한다. 이제 post_list(81째 줄)로 이동한다.

        # 3.1 만약 게시물이 2개 있다면, 129. 이와같이 2개의 쿼리문을 입력한다. (models의 내용을 기반으로 한다.)
        post_001 = Post.objects.create(
            title='첫 번째 포스트 입니다.',
            content='Hello, World. We are the World.',
        )
        post_002 = Post.objects.create(
            title='두 번째 포스트 입니다.',
            content='저는 쌀국수를 좋아합니다. ',
        )
        self.assertEqual(Post.objects.count(), 2) #130. 게시물을 카운트 해 봤을때 2개와 같은(self.assertEqual)지 확인한다.

        # 3.2 포스트 목록 페이지를 새로 고침했을 때,
        response = self.client.get('/blog/') #131.blog페이지를 요청
        soup = BeautifulSoup(response.content, 'html.parser') #132. 다시 response(요청)를 했으니까 soup을 다시 받아와야 한다.
        # 3.3 메인 영역에 포스트 2개의 타이틀이 존재한다.
        main_area = soup.find('div', id='main-area') #133. main-area 지정한 문장을 갖다붙이고,
        self.assertIn(post_001.title, main_area.text) #134. post_001의 타이틀이 main-area의 text안에서 있는지 확인
        self.assertIn(post_002.title, main_area.text) #135. post_002의 타이틀이 main-area의 text안에서 있는지 확인
        # 3.4 "아직 게시물이 없습니다" 라는 문구가 없어야 한다.
        self.assertNotIn('아직 게시물이 없습니다', main_area.text) #136. 이 문구가 없어야(self.assertNotIn) 한다. 이제 test를 해 보고 확인한다.