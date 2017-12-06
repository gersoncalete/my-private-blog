from .base import *
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k6v=%*r@g0kfw(ey%zl@e=7_q4l$j&@u-+!cj4n#kq)i+58qsb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myprivateblog',
        'USER': 'fabio',
        'PASSWORD': 'makaveli',
        'HOST': 'localhost',
        'PORT': '',
    }
}



db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
