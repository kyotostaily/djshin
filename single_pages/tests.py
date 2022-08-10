from django.test import TestCase, Client
from django.contrib.auth.models import User
from blog.models import Post #635.
from bs4 import BeautifulSoup #636. 이것도 blog/tests.py의 4째줄에 가서 복사해 붙여넣어 임포트한다. 이제 44줄로 이동한다.


class TestView(TestCase): #630. 대문자 Test로 시작해야 된다.
    def setUp(self): #631. setUp으로 기본 사항을 만들어 준다.
        self.client = Client() #632. Client를 임포트 한다.
        self.user_trump = User.objects.create_user( #633. user를 blog/tests.py의 3째줄을 복사해와서 임포트 하고, trump에 대한 내용(blog/tests.py의 11~13내용)도 복사해 온다.
            username='trump',
            password='somepassword'
        )

    def test_landing(self): #634. landing에 대한 테스트에 대한 함수를 이와같이 입력한다. 여기선 임의로 총 4개의 포스트(16~38)를 작성해본다.
        post_001 = Post.objects.create( #635. Post는 blog 앱에 있는 모델을 가져와 임포트한다.
            title='첫 번째 포스트',
            content='첫 번째 포스트입니다.',
            author=self.user_trump
        )

        post_002 = Post.objects.create(
            title='두 번째 포스트',
            content='두 번째 포스트입니다.',
            author=self.user_trump
        )

        post_003 = Post.objects.create(
            title='세 번째 포스트',
            content='세 번째 포스트입니다.',
            author=self.user_trump
        )

        post_004 = Post.objects.create(
            title='네 번째 포스트',
            content='네 번째 포스트입니다.',
            author=self.user_trump
        )

        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        body = soup.body #637. beautifulsoup의 기능을 가져오고 soup.body로 body태그 안의 내용을 가져온다.
        self.assertNotIn(post_001.title, body.text) #638. 대문화면에 4 3 2 이 순서로 보여야 하므로 여기서의 1번은 보이면 안된다. 그래서 assertNotIn이다.
        self.assertIn(post_002.title, body.text)
        self.assertIn(post_003.title, body.text)
        self.assertIn(post_004.title, body.text) #638. 이제 single_pages/views.py의 6째줄로 이동한다.
