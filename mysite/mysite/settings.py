"""
이 프로젝트에 대한 장고 설정 파일.
설치된 앱 관리, 템플릿 엔진 적용, 데이터베이스 접속 정보 기록 등 각종 설정 데이터를 작성한다.
manage.py 등의 다른 파일에서 사용된다.

이 설정 파일에 대한 상세 설명.
https://docs.djangoproject.com/en/4.0/topics/settings/

이 파일에서 설정할 수 있는 모든 항목에 대해 살펴보기.
https://docs.djangoproject.com/en/4.0/ref/settings/
"""


##################################################


from pathlib import Path

# BASE_DIR: 이 프로젝트의 root directory. 또한 manage.py 파일이 위치한 경로이기도 하다.
# Python 표준 라이브러리 중 하나인 Path 클래스를 사용했기 때문에, / 연산자로 하위 경로를 표현할 수 있다. ex) BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent


##################################################


# 이하의 설정들은 빠른 개발을 돕기 위한 설정들이다.
# 실제 서비스하는 제품에 적용할 때 주의해서 사용해야 한다.
# 프로젝트를 배포하기 전, 보안 상의 항목들을 위반하지 않는지 점검하는 방법에 대한 설명.
# https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECRET_KEY: 각종 암호화 기능에 사용되는 KEY. 임의의 50글자로 이루어진 문자열이다.
# 따로 설정하지 않는 경우, 기본 값은 빈 문자열('')이지만 그러면 프로젝트가 정상적으로 동작하지 않는다.
SECRET_KEY = 'django-insecure-$r3m#9%3+v%k+h85$&@^e54vuoe0l$jhc)gs$v@nn92ul8f-vx'

# DEBUG: 디버그 모드를 켜고 끄는 논리 값. 디버그 모드가 켜져 있으면 웹 페이지에서 상세한 오류 메시지를 확인할 수 있다.
# 이 값이 False인 경우, 하단의 ALLOWED_HOSTS의 값을 설정해야 한다.
DEBUG = True

# ALLOWED_HOSTS: 이 장고 사이트가 서비스될 수 있는 호스트/도메인 목록.
ALLOWED_HOSTS = []


##################################################


# 이하의 설정들은 애플리케이션과 관련된 설정들이다.

# INSTALLED_APPS: 이 프로젝트에 설치된 앱의 목록.
# 생성한 앱에 대해 마이그레이션을 적용시키려면 여기에 등록해야 한다.
# 장고에서 취급하는 애플리케이션의 개념과 관련 문법.
# https://docs.djangoproject.com/en/4.0/ref/applications/
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# MIDDLEWARE: 요청과 응답을 처리할 때, 그 사이에서 특별한 기능을 하는 클래스들의 목록.
# 보안, 세션, 인증 등의 기능을 가지고 있다.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT_URLCONF: 요청 URL을 처리할 때 사용하기 위한, 핵심 URL구성(URLconf) 파일의 위치.
# 장고에서 요청을 처리하는 과정.
# https://docs.djangoproject.com/en/4.0/topics/http/urls/#how-django-processes-a-request
ROOT_URLCONF = 'mysite.urls'

# TEMPLATES: 이 프로젝트에서 사용할 템플릿 엔진들의 목록.
# 하나의 프로젝트에 여러 개의 템플릿 엔진을 적용할 수도 있으며, 이 때는 각각의 항목들을 dict로 표현한 뒤 list로 묶어서 작성한다.
# # BACKEND: 템플릿 엔진 이름. 기본 엔진으로 DjangoTemplates와 Jinja2가 제공된다.
# # DIRS: 엔진이 템플릿 소스 파일(*.html 파일)을 찾는 경로.
# # APP_DIRS: 설치된 앱 폴더 내부에서 템플릿 소스 파일을 찾을지 여부. 기본 값은 False다.
# # OPTIONS: 기타 설정들. 템플릿 엔진의 종류마다 설정할 수 있는 값이 다르다.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# WSGI_APPLICATION: 장고 내장 서버에서 사용할 WSGI 애플리케이션 객체의 경로. 서버가 가동될 때 사용된다.
WSGI_APPLICATION = 'mysite.wsgi.application'


##################################################


# 이하의 설정들은 데이터베이스와 관련된 설정들이다.

# DATABASES: 프로젝트에서 사용할 데이터베이스들의 목록.
# 최소 1개의 default 데이터베이스를 반드시 설정해야 하며, 필요하면 더 추가할 수 있다.
# # ENGINE: 사용할 데이터베이스 백엔드. 기본적으로 postgresql, mysql, sqlite3, oracle을 제공한다.
# # NAME: 사용할 데이터베이스 이름.
# 데이터베이스의 종류에 따라서 USER, PASSWORD, HOST, PORT 등의 정보를 요구할 수도 있다.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


##################################################


# 비밀번호 검증 관련 설정.
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS: 사용자의 비밀번호에 대해 강력한 정도를 검사하는 검증기들의 목록.
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


##################################################


# 국제화(Internationalization) 및 현지화(Localization).
# 세계 공용 규격에 맞춰, SW국제화를 구현하기 위한 설정들.
# 또는 서버가 서비스되는 지역에 맞춘 설정들.
# https://docs.djangoproject.com/en/4.0/topics/i18n/

# LANGUAGE_CODE: 이 프로젝트에 대한 언어 코드를 나타내는 문자열. 기본 값은 'en-us'.
# 만약 로케일 미들웨어를 사용하지 않는 경우, 이 설정은 모든 사용자에게 제공되는 번역 언어를 결정한다.
# 만약 로케일 미들웨어가 활성 상태여도 사용자의 기본 언어를 확인할 수 없거나 웹 사이트에서 지원하지 않는 경우에 대비하여 예비/대체 언어를 제공한다.
# 반드시 표준 언어 ID 형식을 따라야 한다. 또한 이 설정이 효과를 나타내려면 하단의 USE_I18N 설정 또한 활성화되어야 한다.
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ko-kr'

# TIME_ZONE: 이 프로젝트에 대한 시간대를 나타내는 문자열. 기본 값은 'America/Chicago'.
# 특히 장고를 윈도우 운영체제에서 실행 중일 때, 이 설정을 시스템 시간대와 일치하도록 설정해야 한다.
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

# 장고의 번역 시스템을 사용할지 여부를 저장하는 논리 값. 기본 값은 True.
# 성능 향상을 위해 설정을 끄기도 한다.
USE_I18N = True

# 날짜-시간(datetime) 객체들이 기본적으로 시간대 정보를 포함할지(timezone-aware) 여부를 지정하는 논리 값. 기본 값은 False.
# 이 값을 True로 설정하면 장고는 내부적으로 시간대 정보를 포함하는 날짜 객체를 사용한다.
# USE_TZ가 False인 경우, 장고는 시간대 정보를 포함하지 않는(naive) 날짜-시간 객체를 사용한다.
# 날짜-시간 객체는 서버가 가동되는 지역의 현지 시간을 기준으로 설정된다.
USE_TZ = True


##################################################


# 정적 파일들(CSS, 자바스크립트, 이미지 등)에 대한 설정.
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# 기본 키에 사용할 기본 필드 자료형.
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
