"""
Django settings for djshin_prj project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os #73.이 항목 추가
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-s(dcji-6x(vwfi17t!58o1yogi$r-9lkz-si2a4-7!+f&4xvgh')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DEBUG', 1))

if os.environ.get('DJANGO_ALLOWED_HOSTS'):
    ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(' ')
else:
    ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions', #206. extensions를 설치했기 때문에 여기에 이렇게 입력을 해 준다. 이후 python manage.py shell_plus를 입력해본다. 이제 tests.py의 19번째 줄로 이동한다.
    'django.contrib.sites', #463. django-allauth에서 찾아서 붙인다.

    'allauth', #464.이것들을 복사해서 붙인다.
    'allauth.account', #464.
    'allauth.socialaccount', #464.
    'allauth.socialaccount.providers.google', #465. 구글 아이디로 로그인 할 경우(다른건 그에 맞는것 찾아서 붙이면 된다.) 이제 139줄로 이동한다.

    'crispy_forms', #445. django-crispy-forms의 설치 가이드에 나온대로 이와같이 입력한다. 이제 130줄로 이동한다.
    'markdownx', #454. 이렇게 붙여넣고 djshin_prj/urls.py에 간다.
    'django_summernote', #711. django-summernote의 메뉴얼대로 붙여넣기 하고 이제djshin_prj/urls.py의 28째줄로 간다.

    'blog',
    'single_pages',
    'board', #672. 게시판을 위해 board를 이와같이 추가하고 makemigrations -> migrate를 진행한다. 이제 board/admin.py으로 이동한다.
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djshin_prj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djshin_prj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('SQL_DATABASE', BASE_DIR / 'db.sqlite3'),
        'USER': os.environ.get('SQL_USER', 'user'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'password'),
        'HOST': os.environ.get('SQL_HOST', 'localhost'),
        'PORT': os.environ.get('SQL_PORT', '5432')
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/' #74.여기에 접근할 수 있게 해 줘라 라고 정의가 되어있다.
STATIC_ROOT = os.path.join(BASE_DIR, '_static')

MEDIA_URL = '/media/' #75.url이 media 라고 오는 경우 media 파일을 가져오라는 거구나 라고 인식
MEDIA_ROOT = os.path.join(BASE_DIR, '_media') #76.파일이 저장되는 경로를 잡아준다. BASE_DIR 뒤에다가 _media를 붙이면 파일을 저장하겠다는 뜻, blog/models.py로 이동한다.

CRISPY_TEMPLATE_PACK = 'bootstrap4' #446. django-crispy-forms의 Template packs에서 CRISPY_TEMPLATE_PACK = 'uni_form' 라는 문장을 복사해서 붙여넣고, 현재는 부트스트랩을 쓰므로 이와같이 입력한다. 447. 이제 crispy사이트 내의 crispy filter로 이동해서 {% load crispy_forms_tags %}을 복사해서 post_form.html의 2째줄에 붙인다.

AUTHENTICATION_BACKENDS = [ #466. django-allauth에서 이 내용들(139~145)을 찾아서 붙인다. 이제 templates를 수정하러 67줄로 이동한다(그러나 확인결과 수정할 내용이 없으므로 가지않는다.) 이제 147줄로 이동한다.
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1 #467. 찾아서 복사해 붙여넣는다.

ACCOUNT_EMAIL_REQUIRED = True #468. 이메일 주소를 받아올껀가
ACCOUNT_EMAIL_VERIFICATION = 'none' #469. 회원가입시 이메일을 보내서 확인하려는것, 지금은 안하므로 none으로 한다. 이제djshin/urls.py의 26째 줄로 이동한다.

LOGIN_REDIRECT_URL = '/blog/' #475. 로그인하면 이 페이지로 오게된다. 대문페이지로 설정하고 싶으면 '/'으로 한다. 이제 navbar.html의 34줄로 이동한다.

X_FRAME_OPTIONS = 'SAMEORIGIN' #719. 같은 서버에서는 X FRAME을 사용하게 해 달라는 내용. 이제 board_detail.html의 12째줄로 이동한다.

SUMMERNOTE_THEME = 'bs4'  # Show summernote with Bootstrap4 #721. django-summernote의 themes와 Options에 가서 bootstarap버전에 맞게 이와같이(158~166) 양식을 찾아 붙인다.

SUMMERNOTE_CONFIG = {
    'summernote': {
        # Change editor size
        'width': '100%',
        'height': '480',
    }
}