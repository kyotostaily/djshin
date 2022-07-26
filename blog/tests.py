from django.test import TestCase, Client #118. Client입력
from django.contrib.auth.models import User #185. models.py에 가서 User의 사용을 위해 복사해서 붙여넣는다.
from bs4 import BeautifulSoup #119.
from .models import Post #120. models도 가져와야 하기에 임포트한다.


class TestView(TestCase): #113. 이런식으로 TestCase를 확장시켜준다.
    def setUp(self): #116. setUp으로 시작한 후 (기본적으로 실행되는 함수이다.)
        self.client = Client() #117. 이렇게 입력하고 위(from)에 TestCase옆에 Client(방문하려는 사람의 브라우저)를 입력한다.
        self.user_trump = User.objects.create_user( #184. 이와같이 입력하고
            username='trump',
            password='somepassword'
        )
        self.user_obama = User.objects.create_user( #186. 위의것처럼 하나 더 만들면 test_post_list에서 유저가 2명인 상태로 테스트를 시작한다. 이제 57줄로 간다.
            username='obama',
            password='somepassword'
        )

    def navbar_test(self, soup): #167.def navbar_test 의 내용을 아래와같이 입력한다. test_라는 단어가 앞에 오면 TestCase에서 하나의 유닛단위로 보기 떄문에 navbar를 먼저 쓴다.
        navbar = soup.nav #168. 이 soup이 있어야 복사한 내용을 쓸 수 있다.
        self.assertIn('Blog', navbar.text) #170. Blog가 있는지 테스트
        self.assertIn('About me', navbar.text) #170. About me가 있는지 테스트, 171. 그리고 다시 37의 내용을 복사 해서 83 ~ 85의 내용을 지우고 그 자리에 붙여넣기 한다.

        logo_btn = navbar.find('a', text='Ds') #173. navbar에서 a태그를 찾는데, text가 Ds인 a태그를 찾는다.
        self.assertEqual(logo_btn.attrs['href'], '/') #174.

        home_btn = navbar.find('a', text='Home') #173. navbar에서 a태그를 찾는데, text가 Home인 a태그를 찾는다.
        self.assertEqual(home_btn.attrs['href'], '/') #174.

        blog_btn = navbar.find('a', text='Blog') #173. navbar에서 a태그를 찾는데, text가 Blog인 a태그를 찾는다.
        self.assertEqual(blog_btn.attrs['href'], '/blog/') #174. 홈이 아니기 때문에 페이지'/blog/'를 입력

        about_me_btn = navbar.find('a', text='About me') #173. navbar에서 a태그를 찾는데, text가 about_me인 a태그를 찾는다.
        self.assertEqual(about_me_btn.attrs['href'], '/about_me/') #174. 홈이 아니기 때문에 페이지'/about_me/'를 입력, 이제 base.html의 13째 줄로 간다.

    def test_post_list(self): #114. 여기서는, 함수를 시작할 때 test_post_list처럼 소문자로 시작한다. 이제 cmder에서 pip install beautifulsoup4(장고에서 웹개발, 파이썬 크롤링 할때 많이쓴다.)를 실행한다.
        # 1.1 포스트 목록 페이지(post list)를 연다. 테스트 할 것들을 이런식 으로 글을 쓰면서 준비를 한다.
        response = self.client.get('/blog/') #115. 서버에다 /blog/라는 url로 요청을 한다.(response)
        # 1.2 정상적으로 페이지가 로드된다.
        self.assertEqual(response.status_code, 200) #118. 200은 response(요청)한 것이 잘 로드되었다는 표시이다.
        # 1.3 페이지의 타이틀에 Blog라는 문구가 있다. 119. 이때 from bs4 import BeautifulSoup으로 임포트한다.
        soup = BeautifulSoup(response.content, 'html.parser') #121. beautifulsoup에서 콘텐츠를 가져오는 것을 response(요청)하는데 그게 html.parser(html형태)이다.
        self.assertIn('Blog', soup.title.text) #122. (바로 위에서 정의된 soup이 가져온) 페이지의 타이틀(title - html요소)의(.text)를 봤을때 Blog라는 문구가 안에 있어야 한다(self.assertIn) 라는 뜻이다.
        # 166. 18 ~ 22의 내용을 잘라내고 10째줄로 가서

        self.navbar_test(soup) # 169. 이것을 입력하면 def post_list상에서 beautiful soup으로 입력한 것을 여기에다 넣어서 def navbar_test로 가서 테스트를 한다.

        # 2.1 게시물이 하나도  없을 때
        self.assertEqual(Post.objects.count(), 0) #125. 게시물을 카운트 해 봤을때 0개와 같은(self.assertEqual)지 확인한다.
        # 2.2 메인 영역에 "아직 게시물이 없습니다" 라는 문구가 나온다.
        main_area = soup.find('div', id='main-area') #127. id 가 main-area라는 것을 가진 div를 찾아라는 뜻이고 그게 main_area이다.
        self.assertIn('아직 게시물이 없습니다', main_area.text) #126. 125의 내용이 확인될 때 이 내용('아직 게시물이 없습니다')이 메인영역(main_area.text) 안에 있어야 한다. 이제 post_list(81째 줄)로 이동한다.

        # 3.1 만약 게시물이 2개 있다면, #129.이와같이 2개의 쿼리문을 입력한다. (models의 내용을 기반으로 한다.)
        post_001 = Post.objects.create(
            title='첫 번째 포스트 입니다.',
            content='Hello, World. We are the World.',
            author=self.user_trump #187. 작성자가 있어야 하는 상황이므로 위에서 입력했던 유저를 각각 입력한다.
        )
        post_002 = Post.objects.create(
            title='두 번째 포스트 입니다.',
            content='저는 쌀국수를 좋아합니다. ',
            author=self.user_obama #187. 작성자가 있어야 하는 상황이므로 위에서 입력했던 유저를 각각 입력한다. 이제 77줄로 내려간다.
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

        self.assertIn(post_001.author.username.upper(), main_area.text) #188. post001의 author에 유저네임이 대문자(upper())로 있었으면 좋겠다는 뜻. 뒤에 main_area.text를 붙인다.
        self.assertIn(post_002.author.username.upper(), main_area.text) #189. post002의 author에 유저네임이 대문자(upper())로 있었으면 좋겠다는 뜻. 뒤에 main_area.text를 붙인다. 이제 post_list.html의 27째 줄로 간다.

    def test_post_detail(self): #137. 위의 테스트 조건과는 다른 것을 한다.
        # 1.1. 포스트가 하나 있다. #139. 아래와 같이 포스트 1개를 만든다.
        post_001 = Post.objects.create(
            title='첫 번째 포스트 입니다.',
            content='Hello, World. We are the World.',
            author=self.user_trump #191. post001에는 trump가 입력되 있으므로 이와같이 입력한다. 이제 107줄로 이동한다.
        )
        self.assertEqual(Post.objects.count(), 1) #138. 게시물을 카운트 해 봤을때 1개와 같은(self.assertEqual)지 확인한다.
        # 1.2. 그 포스트의 url은 ‘/blog/1/’ 이다.
        self.assertEqual(post_001.get_absolute_url(), '/blog/1/') #140. url을 알려면 get_absolute_url()을 입력하고 뒤에 확인할 url을 입력한다.

        # 2. 첫 번째 포스트의 상세 페이지 테스트
        # 2.1. 첫 번째 포스트의 url로 접근하면 정상적으로 response가 온다(status code: 200).
        response = self.client.get(post_001.get_absolute_url()) #141
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        # 2.2. 포스트 목록 페이지와 똑같은 내비게이션 바가 있다.
        self.navbar_test(soup) #172. 기존의 83~85내용을 지우고 37의 내용을 붙여넣기 한다.(이것을 입력하면 def test_post_detail상에서 beautiful soup으로 입력한 것을 여기에다 넣어서 def navbar_test로 가서 테스트를 한다.) 이제 15줄로 이동한다.

        # 2.3. 첫 번째 포스트의 제목이 웹 브라우저 탭 타이틀에 들어 있다.
        self.assertIn(post_001.title, soup.title.text) #144. post_001의 타이틀이 soup에 있어야 한다는 뜻 161. 맨뒤에 .text를 추가한다(글자가 있는지 보기 위해서) 이제 post_detail.html의 8째줄로 이동한다.
        # 2.4. 첫 번째 포스트의 제목이 포스트 영역에 있다.
        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id='post-area') #145. post_area는 main_area 안에 있고 id는 post-area다. 이렇게 안되있으면 html파일을 열어서 고쳐야된다.
        self.assertIn(post_001.title, post_area.text) #146. post_001의 title이 post_area.text 안에(self.assertIn) 있다는 뜻
        # 2.5. 첫 번째 포스트의 작성자(author)가 포스트 영역에 있다(아직 구현할 수 없음).
        self.assertIn(self.user_trump.username.upper(), post_area.text) #192. 이 내용이 post_area안에 있으면 좋겠다는 뜻이다. 이제 post_detail.html의 18번째 줄로 간다.
        # 2.6. 첫 번째 포스트의 내용(content)이 포스트 영역에 있다.
        self.assertIn(post_001.content, post_area.text) #147. post_001의 content가 post_area.text 안에(self.assertIn) 있다는 뜻, 148.post_list.html 파일을 복사해서 post_list.html이 있는 blog폴더에 붙여넣기를 하면서, base.html로 지정하고 들어간다.