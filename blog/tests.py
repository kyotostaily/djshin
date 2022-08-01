from django.test import TestCase, Client #118. Client입력
from django.contrib.auth.models import User #185. models.py에 가서 User의 사용을 위해 복사해서 붙여넣는다.
from bs4 import BeautifulSoup #119.
from .models import Post, Category, Tag #120. models도 가져와야 하기에 임포트한다. 208. Category를 임포트한다. 305. Tag를 임포트한다.


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
        self.user_obama.is_staff = True #366. obama는 스태프권한이 있는 상태라는 뜻
        self.user_obama.save() #367. save를 해 준다. 이제 214줄로 이동한다.

        self.category_programming = Category.objects.create( #207. 테스트 목적으로 programming이라는 카테고리를 만든다. 여기서 self를 붙이는 이유는 이걸 붙여야 이 안에 다른 테스트 항목에서도 적용될수 있기 때문이다.
            name='programming', slug='programming' #209. 이름과 슬러그를 programming으로 지정한다(왜냐면 지금은 admin에서 만드는게 아니기 때문에 직접 지정해 줘야하기 때문이다.)
        )
        self.category_music = Category.objects.create( #210. 뮤직 카테고리를 만든다.
            name='music', slug='music' #210. 이렇게 만들고 80~89의 내용을 잘라내고(그 위의 주석은 지우고), 26열에 붙여넣는다.
        )

        self.tag_python_kor = Tag.objects.create( #305. Tag의 테스트를 위해 26~34와 같이 입력하고, 위에 Tag를 임포트 한다.
            name='파이썬 공부', slug='파이썬-공부' #306. tag_python_kor 라는 Tag
        )
        self.tag_python = Tag.objects.create(
            name='python', slug='python' #307. tag_python이라는 Tag
        )
        self.tag_hello = Tag.objects.create(
            name='hello', slug='hello' #308. tag_hello라는 Tag, 이제 42째 줄로 이동한다.
        )

        self.post_001 = Post.objects.create( #211.접근을 위해 앞에 self를 붙여준다.
            title='첫 번째 포스트 입니다.',
            content='Hello, World. We are the World.',
            category=self.category_programming, #214. 카테고리가 프로그래밍으로 붙여줌
            author=self.user_trump  # 187. 작성자가 있어야 하는 상황이므로 위에서 입력했던 유저를 각각 입력한다.
        )
        self.post_001.tags.add(self.tag_hello) #309. 이것을 입력함으로 ManytoManyField에 하나가 추가된것이다.

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
        self.post_003.tags.add(self.tag_python_kor) #310. 위에 29, 32에 입력했던 태그들을 이곳에 입력한다.
        self.post_003.tags.add(self.tag_python) #310. 위에 29, 32에 입력했던 태그들을 이곳에 입력한다. 이제 110줄로 이동한다.

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
        self.assertIn(self.tag_hello.name, post_001_card.text) #311. assertIn을 사용해서 태그가 이와같이 있어야 한다는 것이다.
        self.assertNotIn(self.tag_python.name, post_001_card.text) #312. assertNotIn을 사용해서 위의 tag_hello외에는 영향이 없게한다.
        self.assertNotIn(self.tag_python_kor.name, post_001_card.text) #312. assertNotIn을 사용해서 위의 tag_hello외에는 영향이 없게한다.

        post_002_card = main_area.find('div', id='post-2') #246.post_002의 card에 관한 것을 main_area안에서 div를 찾는데, id는 post-2인것.
        self.assertIn(self.post_002.title, post_002_card.text) #135. post_002의 타이틀이 main-area의 text안에서 있는지 확인 233.self를 붙여준다. 245. main-area를 post_002_card로 바꿔준다.
        self.assertIn(self.post_002.category.name, post_002_card.text) #250. self.post_002.category.name이 self.post_002_card 안에 있기를 바라는 것이다.
        self.assertNotIn(self.tag_hello.name, post_002_card.text) #313. 여기는 태그된게 없기 때문에 세줄 전부 assertNotIn으로 해야된다.
        self.assertNotIn(self.tag_python.name, post_002_card.text) #313.
        self.assertNotIn(self.tag_python_kor.name, post_002_card.text) #313.

        post_003_card = main_area.find('div', id='post-3') #247. post_003의 card에 관한 것을 main_area안에서 div를 찾는데, id는 post-3인것.
        self.assertIn(self.post_003.title, post_003_card.text) #248. main-area를 post_003_card로 바꿔준다. (이렇게 하면 post_list.html에 card가 3개가 나타나고 title이 제대로 들어가 있는지 확인을 한다.)
        self.assertIn('미분류', post_003_card.text) #251.post_003_card에는 카테고리가 없기 때문에, 없는 경우에는 미분류로 표시 해준다. 이제 62줄로 이동한다.
        self.assertNotIn(self.tag_hello.name, post_003_card.text) #314.tag_hello는 여기선 영향을 미치면 안되므로 assertNotIn
        self.assertIn(self.tag_python.name, post_003_card.text) #315. tag_python은 여기에 태그되있으므로 assertIn
        self.assertIn(self.tag_python_kor.name, post_003_card.text) #316. tag_python_kor또한 여기에 태그되 있으므로 assertIn. 이제 post_list.html의 33째줄로 간다.

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
        self.category_card_test(soup) #274. post_detail.html페이지를 위한 category_card_test를 추가한다.

        self.assertIn(self.post_001.title, soup.title.text) #239. self를 붙인다.

        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id='post-area') #145. post_area는 main_area 안에 있고 id는 post-area다. 이렇게 안되있으면 html파일을 열어서 고쳐야된다.
        self.assertIn(self.post_001.title, post_area.text) #240. self를 붙인다.
        self.assertIn(self.post_001.category.name, post_area.text) #275. post-area의 카테고리에 네임이 있어야 한다. 이제 views.py의 21째 줄로 이동한다.

        self.assertIn(self.user_trump.username.upper(), post_area.text) #192. 이 내용이 post_area안에 있으면 좋겠다는 뜻이다. 이제 post_detail.html의 18번째 줄로 간다.
        self.assertIn(self.post_001.content, post_area.text) #241.self를 붙이고 74줄로 이동한다.

        self.assertIn(self.tag_hello.name, post_area.text) #318. 110~112의 내용을 복사해서 붙이고, post_area로 변경하여 테스트한다.
        self.assertNotIn(self.tag_python.name, post_area.text) #318
        self.assertNotIn(self.tag_python_kor.name, post_area.text) #318. 이후 post_detail.html의 45째줄로 이동한다.

    def test_category_page(self): #278. category_page의 테스트코드를 작성한다.
        response = self.client.get(self.category_programming.get_absolute_url()) #279 해당하는 카테고리에 absolute_url을 통해서 가도록 만든다.
        self.assertEqual(response.status_code, 200) #280. 잘나오는지 200인지 확인하고,

        soup = BeautifulSoup(response.content, 'html.parser') #281. soup을 써야 여러 필요한 것들을 불러올수 있고 html.parser를 써서 soup에다가 담아준다.
        self.navbar_test(soup) #282. soup넣고 navbar테스트 하고
        self.category_card_test(soup) #283. 여기도 soup넣고 카테고리 카드 테스트도 한다.(카테고리 페이지가 만들어지면서, post_list의 화면 분할이 해결이 되었다.

        main_area = soup.find('div', id='main-area') #284. 139째줄의 내용을 복사해서 붙인다.(div로 되어있는 id가 main-area인 것을 가져와라)
        self.assertIn(self.category_programming.name, main_area.h1.text) #285. main-area의 h1에 programming.name이 있어야 한다.
        self.assertIn(self.category_programming.name, main_area.text) #288. main-area에 programming.name이 있어야 한다. 이제 models.py의 13째 줄로 이동한다.
        self.assertIn(self.post_001.title, main_area.text) #286.setup에서 programming은 post_001하나밖에 없으므로, 이것 하나만 입력한다.
        self.assertNotIn(self.post_002.title, main_area.text) #287. 여기서 002와 003은 보이면 안되므로 NotIn을 붙여준다.
        self.assertNotIn(self.post_003.title, main_area.text) #287. 여기서 002와 003은 보이면 안되므로 NotIn을 붙여준다. 이제 155줄로 이동한다.

    def test_tag_page(self): #320.174의 내용을 가져와서 test_tag_page 라는 테스트 함수를 만들고 아래와같이 입력한다.
        response = self.client.get(self.tag_hello.get_absolute_url()) #321카테고리가 아닌 tag_hello의 절대경로 get_absolute_url()로 가게 한다.
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.navbar_test(soup)
        self.category_card_test(soup)

        self.assertIn(self.tag_hello.name, soup.h1.text)
        main_area = soup.find('div', id='main-area')
        self.assertIn(self.tag_hello.name, main_area.text)

        self.assertIn(self.post_001.title, main_area.text) #322. tag_hello가 달려있는 것은 post_001뿐이므로 이것만 assertIn을 해주고
        self.assertNotIn(self.post_002.title, main_area.text) #323. 이것들은 없으므로 assertNotIn
        self.assertNotIn(self.post_003.title, main_area.text) #323. 이것들은 없으므로 assertNotIn. 이제 blog/urls.py의 5째줄로 이동한다.

    def test_create_post_without_login(self): #345. test_create_post_without_login로 이름을 바꾼다.
        response = self.client.get('/blog/create_post/')
        self.assertNotEqual(response.status_code, 200) #346. 로그인 없이 접근시 200이 되면 안된다.

    def test_create_post_with_login(self): #347. 로그인 했을 경우(테스트)
        self.client.login(username='trump', password='somepassword') #348. 유저네임과 비번 설정된 상태에서
        response = self.client.get('/blog/create_post/') #349. 이곳으로 잘 가야된다. 이제 views.py의 3째줄로 이동한다.
        self.assertNotEqual(response.status_code, 200) #368. trump는 스태프가 아니므로 assertNotEqual이 되야한다.

        self.client.login(username='obama', password='somepassword') #369. trump대신 obama를 입력하고
        response = self.client.get('/blog/create_post/') #370. 이 경로로 잘 가야되며
        self.assertEqual(response.status_code, 200) #371. obama는 현재 스태프 권한이 있으므로 assertEqueal이 되어야 한다. 235줄로 이동한다.

        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual('Create Post - Blog', soup.title.text)
        main_area = soup.find('div', id='main-area')
        self.assertIn('Create a New Post', main_area.text)

        tag_str_input = main_area.find('input', id='id_tags_str') #404. input태그 중에서 id로 id_tags_str이 있는지 테스트(post_form.html의 14번쨰 줄에 있는 id가 있는지 확인)
        self.assertTrue(tag_str_input) #405. tag_str_input이 있는지 확인하고
        self.assertEqual(Tag.objects.count(), 3)

        self.client.post( #352. 윗 내용에 들어가는 것을 딕셔너리 형태로 아래와 같이 입력한다. 221 ~ 226
            '/blog/create_post/',
            {
                'title': 'Post Form 만들기',
                'content': 'Post Form 페이지를 만듭시다.',
                'tags_str': 'new tag; 한글 태그, python' #406. 있으면 이와같이 세개의 태그가 추가가 되도록 입력 해서 시험해본다.(결과적으로, python이라는 태그는 이미 위에 32째줄에 있으니 그대로 있고, 나머지 두개의 태그만 추가된다.) 이것을 post형태로 서버에 보내주게 된다. 이제 243줄로 이동한다.
            }
        )

        last_post = Post.objects.last() #356. 맨 마지막 포스트를 가져와라
        self.assertEqual(last_post.title, 'Post Form 만들기') #357. last_post.title의 내용
        self.assertEqual(last_post.author.username, 'obama') #372. 스태프가 obama이므로 바꿔준다. 이제 views.py의 29번째줄로 이동한다.
        self.assertEqual(last_post.content, 'Post Form 페이지를 만듭시다.') #359. " "의 내용. 이제 views.py의 33째줄로 간다.

        self.assertEqual(last_post.tags.count(), 3) #407. last_post에 tags는 3개다 라는 뜻
        self.assertTrue(Tag.objects.get(name='new tag')) #408. 이러한 태그들이 db에 저장이 되어있는지 확인(db에 있다면 가져올 수 있다.)
        self.assertTrue(Tag.objects.get(name='한글 태그')) #408.
        self.assertTrue(Tag.objects.get(name='python')) #408.
        self.assertEqual(Tag.objects.count(), 5) #409.윗쪽에 원래 태그가 3개였는데 태그가 2개가 더 추가 되서 5개가 되었기 때문에 5개인지 확인, 이제 views.py의 410번으로 이동한다.

    def test_update_post(self): #378. update_post상황에 대한 테스트코드(238~275)
        update_post_url = f'/blog/update_post/{self.post_003.pk}/' #379.post_003의 해당 포스트를 들어서 테스트한다는뜻, 383.urls.py의 5째줄에 가서 이것에 대한 경로를 잡아준다.

        # 380.로그인 하지 않은 상태에서 접근 하는 경우
        response = self.client.get(update_post_url)
        self.assertNotEqual(response.status_code, 200)

        # 381.로그인은 했지만, 작성자가 아닌 경우
        self.assertNotEqual(self.post_003.author, self.user_trump) #381. trump는 아니므로 NotEqual
        self.client.login(username='trump', password='somepassword')
        response = self.client.get(update_post_url)
        self.assertNotEqual(response.status_code, 200)

        # 382.작성자(obama)가 접근하는 경우
        self.assertEqual(self.post_003.author, self.user_obama) #382. 세번째 포스트의 obama이므로 맞으므로 assertEqual이 맞다.
        self.client.login(username='obama', password='somepassword')
        response = self.client.get(update_post_url)
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser') #391.soup을 받아준 후

        self.assertEqual('Edit Post - Blog', soup.title.text) #392. Edit Post - Blog로 나오면 좋겠다고 입력후 아래와같이입력(259~275)
        main_area = soup.find('div', id='main-area')
        self.assertIn('Edit Post', main_area.text) #393. 이와같이 입력 후, post_form을 복사해서 post_update_form.html을 만들고 views.py의 49째 줄로 이동한다.

        response = self.client.post( #397. 세번째 포스트의 내용(53~57)을 수정하는 것을 테스트 한다.
            update_post_url,
            {
                'title': '세 번째 포스트를 수정했습니다.',
                'content': '안녕 세계? 우리는 하나!',
                'category': self.category_music.pk #397. pk를 적어줘야 번호로 찾아준다.
            },
            follow=True #398. redirect되는것까지 쫓아가게 하기 위해 입력한다.
        )
        soup = BeautifulSoup(response.content, 'html.parser')
        main_area = soup.find('div', id='main-area')
        self.assertIn('세 번째 포스트를 수정했습니다.', main_area.text) #399. 위의 내용을 입력해서 이 내용이 있었음 좋겠다.
        self.assertIn('안녕 세계? 우리는 하나!', main_area.text) #399. 위의 내용을 입력해서 이 내용이 있었음 좋겠다.
        self.assertIn(self.category_music.name, main_area.text) #399. 위의 내용을 입력해서 이 내용이 있었음 좋겠다. 이제 post_detail.html의 28째 줄로 이동한다.