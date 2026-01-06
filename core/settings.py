"""
Django settings for the project.

Updated for UniKL Secure Software Development Project.
Folder Name: core
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY WARNING: keep the secret key used in production secret! ---
SECRET_KEY = 'django-insecure-ganti-dengan-kunci-rahsia-anda-di-sini'

# --- SECURITY WARNING: don't run with debug turned on in production! ---
DEBUG = True 

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # --- APPS ANDA (Wajib Ada) ---
    'accounts',  # Untuk Login/Register/AuditLog/Profile
    'core',      # Untuk Dashboard & Settings Utama
    'tasks',     # Untuk CRUD Task
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

# Config URL Utama
ROOT_URLCONF = 'core.urls' 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Folder templates di root
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

# Config WSGI
WSGI_APPLICATION = 'core.wsgi.application' 

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- PENTING: BERITAHU DJANGO GUNA MODEL USER KITA ---
AUTH_USER_MODEL = 'accounts.CustomUser'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ==============================================================================
# KONFIGURASI STATIC & MEDIA (GAMBAR) - Wajib untuk Profile Picture
# ==============================================================================

# Static files (CSS, JavaScript, Images System)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files (Gambar User Upload / Profile Picture)
# Ini bahagian BARU yang ditambah
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==============================================================================
# KONFIGURASI KESELAMATAN TAMBAHAN
# ==============================================================================

# 1. Login Redirect (Lepas login nak pergi mana)
LOGIN_REDIRECT_URL = 'user_dashboard'
LOGOUT_REDIRECT_URL = 'login_view'
LOGIN_URL = 'login_view'

# 2. Session Security (Cookies)
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# 3. HTTPS Settings (False untuk localhost)
SESSION_COOKIE_SECURE = False  
CSRF_COOKIE_SECURE = False