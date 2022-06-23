"""
이 프로젝트에 대한 장고 설정 파일.
설치된 앱의 목록, 데이터베이스 접속 정보, 비밀번호 검증 클래스 등의 각종 설정 정보를 기록한다.
manage.py 등의 파일에서 불러져서 사용된다.

설정 파일에 대한 상세 설명.
https://docs.djangoproject.com/en/4.0/topics/settings/

이 파일에서 설정할 수 있는 항목에 대해 살펴보기.
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

##################################################

from pathlib import Path

# 이 프로젝트의 build path이자 manage.py 파일이 위치한 경로.
# Python 표준 라이브러리에 속하는 Path 객체를 사용했기 때문에, / 연산자로 하위 경로를 표현할 수 있다. ex) BASE_DIR / 'mysite'
BASE_DIR = Path(__file__).resolve().parent.parent

##################################################

# 빠른 개발을 위한 설정. 당연히 실제 서비스하는 제품에 적용하면 안 된다.
# 하단의 링크를 통해, 배포 전에 보안 상의 항목들을 위반하지 않는지 점검할 수 있는 기능에 대해 자세히 살펴볼 수 있다.
# https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# 각종 암호화 기능에 사용되는 KEY. 임의의 50글자로 이루어진 문자열이다.
# 따로 설정하지 않는 경우 기본 값은 ''이지만, 그러면 프로젝트가 구동되지 않는다.
SECRET_KEY = 'django-insecure-d75q2=lzx=ka)zwzl9kpro2&d-mc3z15-)g)=!6a)ii!3$vq2e'

# 디버그 모드를 켜고 끄는 설정 값. 디버그 모드가 켜져 있으면 상세한 오류 메시지를 확인할 수 있다.
# 이 값이 False인 경우, 하단의 ALLOWED_HOSTS의 값을 설정해야 한다.
DEBUG = True

# 이 장고 사이트가 서비스될 수 있는 호스트/도메인 목록.
ALLOWED_HOSTS = []

##################################################

# 애플리케이션 정의 관련 설정.

# 이 프로젝트에 설치된 앱의 목록. 생성한 앱을 프로젝트에 적용시키려면 반드시 여기에 등록해야 한다.
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 요청과 응답을 처리할 때, 그 사이에서 특별한 기능을 하는 클래스들의 목록. 보안, 세션, 인증 등의 기능을 가지고 있다.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 요청 URL을 처리할 때 사용하기 위한, 가장 기본적인 URL 구성 파일의 위치.
ROOT_URLCONF = 'mysite.urls'

# 이 프로젝트에서 사용할 템플릿 엔진들의 목록. 각각의 항목들을 dict로 표현한 뒤 list로 묶어서 작성한다.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # 템플릿 엔진 이름.
        'DIRS': [], # 엔진이 템플릿 소스 파일(*.html 파일)을 찾는 경로.
        'APP_DIRS': True, # 설치된 애플리케이션 폴더 내부에서 템플릿 소스 파일을 찾을지 여부.
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        }, # 기타 설정들. 각 템플릿 엔진마다 설정할 수 있는 값이 다르다.
    },
]

# 장고 내장 서버에서 사용할 WSGI 애플리케이션 객체의 경로. 서버가 가동될 때 사용한다.
WSGI_APPLICATION = 'mysite.wsgi.application'

##################################################

# 데이터베이스 관련 설정.

# 설명
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

##################################################

# 비밀번호 검증 관련 설정.
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

# 설명
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

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

##################################################

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
