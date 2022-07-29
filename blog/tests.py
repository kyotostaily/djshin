from django.test import TestCase, Client #118. Client입력
from django.contrib.auth.models import User #185. models.py에 가서 User의 사용을 위해 복사해서 붙여넣는다.
from bs4 import BeautifulSoup #119.
from .models import Post, Category #120. models도 가져와야 하기에 임포트한다. 208. Category를 임포트한다.


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

        self.category_programming = Category.objects.create( #207. 테스트 목적으로 programming이라는 카테고리를 만든다. 여기서 self를 붙이는 이유는 이걸 붙여야 이 안에 다른 테스트 항목에서도 적용될수 있기 때문이다.
            name='programming', slug='programming' #209. 이름과 슬러그를 programming으로 지정한다(왜냐면 지금은 admin에서 만드는게 아니기 때문에 직접 지정해 줘야하기 때문이다.)
        )
        self.category_music = Category.objects.create( #210. 뮤직 카테고리를 만든다.
            name='music', slug='music' #210. 이렇게 만들고 80~89의 내용을 잘라내고(그 위의 주석은 지우고), 26열에 붙여넣는다.
        )

        self.post_001 = Post.objects.create( #211.접근을 위해 앞에 self를 붙여준다.
            title='첫 번째 포스트 입니다.',
            content='Hello, World. We are the World.',
            category=self.category_programming, #214. 카테고리가 프로그래밍으로 붙여줌
            author=self.user_trump  # 187. 작성자가 있어야 하는 상황이므로 위에서 입력했던 유저를 각각 입력한다.
        )
        self.post_002 = Post.objects.create( #212.접근을 위해 앞에 self를 붙여준다.
            title='두 번째 포스트 입니다.',
            content='저는 쌀국수를 좋아합니다. ',
            category=self.category_music, #215. 카테고리가 뮤직으로 붙여줌, 이제 80줄로 이동한다.
            author=self.user_obama  # 187. 작성자가 있어야 하는 상황이므로 위에서 입력했던 유저를 각각 입력한다. 이제 77줄로 내려간다.
        )

        self.post_003 = Post.objects.create( #213.하나 더 만들고 접근을 위해 앞에 self를 붙여준다.
            title='세 번째 포스트 입니다.',
            content='Category가 없을 수도 있죠.',
            author=self.user_obama
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

    def category_card_test(self, soup): #252. 위의 navbar_test와 같이 soup을 받아서 아래와같이 함수를 작성한다.
        categories_card = soup.find('div', id='categories-card') #253. soup.find에서 div를 찾는데 base.html에서 id가 categories-card인 것을 찾는다.
        self.assertIn('Categories', categories_card.text) #254. categories_card에 Categories라는 문구가 있는지 확인
        self.assertIn(
            f'{self.category_programming} ({self.category_programming.post_set.count()})',
            categories_card.text
        ) #255. categories_card안에 programming이 있는지 확인 (setup에서 programming, music과 미분류 항목이 있기때문에 이렇게 지정)
        self.assertIn(
            f'{self.category_music} ({self.category_music.post_set.count()})',
            categories_card.text
        ) #256. categories_card안에 music이 있는지 확인
        self.assertIn(
            f'미분류 ({Post.objects.filter(category=None).count()})',
            categories_card.text
        ) #257. categories_card안에 미분류가 있는지 확인후 88줄로 이동한다.

    def test_post_list_with_posts(self): #114.(229.아래와같이 정리하며 확인한다.) 여기서는, 함수를 시작할 때 test_post_list처럼 소문자로 시작한다. 이제 cmder에서 pip install beautifulsoup4(장고에서 웹개발, 파이썬 크롤링 할때 많이쓴다.)를 실행한다. 217.이와같이 이름을 바꿔주고(포스트가 있을때의 함수) 95번째 줄로 이동한다.
        self.assertEqual(Post.objects.count(), 3)#216.(230.이 문장을 여기로 옮겨준다.) 카테고리가 3개이므로 숫자를 3으로 바꿔준다. 이제 62줄로 이동한다.

        response = self.client.get('/blog/') #115. 서버에다 /blog/라는 url로 요청을 한다.(response)
        self.assertEqual(response.status_code, 200) #118. 200은 response(요청)한 것이 잘 로드되었다는 표시이다.

        soup = BeautifulSoup(response.content, 'html.parser') #121. beautifulsoup에서 콘텐츠를 가져오는 것을 response(요청)하는데 그게 html.parser(html형태)이다.
        self.assertIn('Blog', soup.title.text) #122. (바로 위에서 정의된 soup이 가져온) 페이지의 타이틀(title - html요소)의(.text)를 봤을때 Blog라는 문구가 안에 있어야 한다(self.assertIn) 라는 뜻이다.

        self.navbar_test(soup) # 169. 이것을 입력하면 def post_list상에서 beautiful soup으로 입력한 것을 여기에다 넣어서 def navbar_test로 가서 테스트를 한다.
        self.category_card_test(soup) #258.category_card_test를 navbar밑에서 하면 되므로 이렇게 입력한다. 이제 base.html의 34줄로 이동한다.
        #231. 73~78 항목 삭제하고,
        main_area = soup.find('div', id='main-area') #133. main-area 지정한 문장을 갖다붙이고,
        self.assertNotIn('아직 게시물이 없습니다', main_area.text) #242. 아랫문장을 이 위치로 옮긴다.

        post_001_card = main_area.find('div', id='post-1') #243.post_001의 card에 관한 것을 main_area안에서 div를 찾는데, id는 post-1인것.
        self.assertIn(self.post_001.title, post_001_card.text) #134. post_001의 타이틀이 main-area의 text안에서 있는지 확인 232.self를 붙여준다. 244. main-area를 post_001_card로 바꿔준다.
        self.assertIn(self.post_001.category.name, post_001_card.text) #249. self.post_001.category.name이 self.post_001_card 안에 있기를 바라는 것이다.

        post_002_card = main_area.find('div', id='post-2') #246.post_002의 card에 관한 것을 main_area안에서 div를 찾는데, id는 post-2인것.
        self.assertIn(self.post_002.title, post_002_card.text) #135. post_002의 타이틀이 main-area의 text안에서 있는지 확인 233.self를 붙여준다. 245. main-area를 post_002_card로 바꿔준다.
        self.assertIn(self.post_002.category.name, post_002_card.text) #250. self.post_002.category.name이 self.post_002_card 안에 있기를 바라는 것이다.

        post_003_card = main_area.find('div', id='post-3') #247. post_003의 card에 관한 것을 main_area안에서 div를 찾는데, id는 post-3인것.
        self.assertIn(self.post_003.title, post_003_card.text) #248. main-area를 post_003_card로 바꿔준다. (이렇게 하면 post_list.html에 card가 3개가 나타나고 title이 제대로 들어가 있는지 확인을 한다.)
        self.assertIn('미분류', post_003_card.text) #251.post_003_card에는 카테고리가 없기 때문에, 없는 경우에는 미분류로 표시 해준다. 이제 62줄로 이동한다.

        self.assertIn(self.post_001.author.username.upper(), main_area.text) #234.self를 붙여준다.
        self.assertIn(self.post_002.author.username.upper(), main_area.text) #235.self를 붙여준다. 이후 104번째 줄로 이동한다.

    def test_post_list_without_post(self): #218. 이와같이 함수를 지정한다(포스트가 없을때의 함수)
        Post.objects.all().delete()  # 219.222. 포스트가 이미 setup에 3개가 있으므로 일단 지워줘야 하므로 이렇게 입력한다. Post.objects.all():db에서 다 가져오란 것이고, delete()는 가져온 것들을 다 지우라는 뜻이다.
        self.assertEqual(Post.objects.count(), 0)  # 220. 74~78의 내용을 잘라서 붙여넣고 이와 같이 만든다. #226. Post가 아무것도 없드는 것을 확인하면서 이 자리에 붙인다.

        response = self.client.get('/blog/') #221. 63~69의 내용을 복사해와서 이와같이 붙인다. 223./blog/로 들어가서 페이지를 읽은다음
        self.assertEqual(response.status_code, 200) #224. 200나오는것 확인하고,

        soup = BeautifulSoup(response.content, 'html.parser')
        self.navbar_test(soup) #228. navbar_test도 불러와서 테스트한다. 이제 62줄로 이동한다.
        self.assertIn('Blog', soup.title.text) #225. Blog가 soup.title에 있는지 확인한 후,

        main_area = soup.find('div', id='main-area') #227.이와 같이 입력하여 메인 영역에 '아직 게시물이 없습니다' 라고 나오게 하면 된다.
        self.assertIn('아직 게시물이 없습니다', main_area.text)

    def test_post_detail(self): #137. 위의 테스트 조건과는 다른 것을 한다.
        self.assertEqual(Post.objects.count(), 3) #236. 98~103내용지우고, 숫자를 3으로 바꾼다.)
        # 1.2. 그 포스트의 url은 ‘/blog/1/’ 이다.
        self.assertEqual(self.post_001.get_absolute_url(), '/blog/1/') #237. post_001을 setup에서 접근하므로 self를 붙여준다.

        # 2. 첫 번째 포스트의 상세 페이지 테스트
        # 2.1. 첫 번째 포스트의 url로 접근하면 정상적으로 response가 온다(status code: 200).
        response = self.client.get(self.post_001.get_absolute_url()) #238 self를 붙인다.
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        # 2.2. 포스트 목록 페이지와 똑같은 내비게이션 바가 있다.
        self.navbar_test(soup) #172. 기존의 83~85내용을 지우고 37의 내용을 붙여넣기 한다.(이것을 입력하면 def test_post_detail상에서 beautiful soup으로 입력한 것을 여기에다 넣어서 def navbar_test로 가서 테스트를 한다.) 이제 15줄로 이동한다.

        # 2.3. 첫 번째 포스트의 제목이 웹 브라우저 탭 타이틀에 들어 있다.
        self.assertIn(self.post_001.title, soup.title.text) #239. self를 붙인다.
        # 2.4. 첫 번째 포스트의 제목이 포스트 영역에 있다.
        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id='post-area') #145. post_area는 main_area 안에 있고 id는 post-area다. 이렇게 안되있으면 html파일을 열어서 고쳐야된다.
        self.assertIn(self.post_001.title, post_area.text) #240. self를 붙인다.
        # 2.5. 첫 번째 포스트의 작성자(author)가 포스트 영역에 있다(아직 구현할 수 없음).
        self.assertIn(self.user_trump.username.upper(), post_area.text) #192. 이 내용이 post_area안에 있으면 좋겠다는 뜻이다. 이제 post_detail.html의 18번째 줄로 간다.
        # 2.6. 첫 번째 포스트의 내용(content)이 포스트 영역에 있다.
        self.assertIn(self.post_001.content, post_area.text) #241.self를 붙이고 74줄로 이동한다.