"""
Django settings for adtest project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import ldap
import os
import logging

logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)



from django_auth_ldap.config import LDAPSearch, NestedActiveDirectoryGroupType

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ww!8@tj63qtkkcbzw+%(kk6=_hn1p_lxq4_zdb4l8g2w$$0+72'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'adtest.urls'

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

WSGI_APPLICATION = 'adtest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Auth to Window Active Directory 2012

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_SERVER_URI = "ldap://ec2-52-49-208-202.eu-west-1.compute.amazonaws.com:389"
AUTH_LDAP_BIND_DN = "LIGHTHOUSE"
AUTH_LDAP_BIND_PASSWORD = "HomeWork2016"
AUTH_LDAP_USER_SEARCH = LDAPSearch("CN=Users,DC=lighthouse,DC=dstl", ldap.SCOPE_SUBTREE, '(SAMAccountName=%(user)s)')
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("CN=Users,DC=lighthouse,DC=dstl", ldap.SCOPE_SUBTREE, "(objectClass=top)")

# Important set group type
AUTH_LDAP_GROUP_TYPE = NestedActiveDirectoryGroupType()

# Cache settings

AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 300



# User flags

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "CN=dstl,CN=Users,DC=lighthouse,DC=dstl",
    "is_staff": "CN=dstl,CN=Users,DC=lighthouse,DC=dstl",
    "is_superuser": "CN=dstl,CN=Users,DC=lighthouse,DC=dstl",
}

# Group mirror

# Important to match the group's permission
AUTH_LDAP_MIRROR_GROUPS = True


AUTH_LDAP_CONNECTION_OPTIONS = {
        ldap.OPT_DEBUG_LEVEL: 1,
        ldap.OPT_REFERRALS: 0,
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
