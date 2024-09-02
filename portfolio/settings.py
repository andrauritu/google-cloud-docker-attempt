import os
from pathlib import Path
import environ
import io

# Initialize environment variables
env = environ.Env(
    DEBUG=(bool, False)
)

# Determine if running in production or locally
IS_PRODUCTION = os.getenv('GOOGLE_CLOUD_PROJECT') is not None

BASE_DIR = Path(__file__).resolve().parent.parent

if IS_PRODUCTION:
    # Import Google Cloud Secret Manager only in production
    from google.cloud import secretmanager
    
    def get_secret(secret_name):
        client = secretmanager.SecretManagerServiceClient()
        project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
        if not project_id:
            raise Exception("GOOGLE_CLOUD_PROJECT environment variable not set.")
        name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
        response = client.access_secret_version(name=name)
        return response.payload.data.decode("UTF-8")
    GS_BUCKET_NAME = env('GS_BUCKET_NAME', default=None)
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    MEDIA_URL = f"https://storage.googleapis.com/{GS_BUCKET_NAME}/"
    print("it thinks its in prod!")

    # Fetch secrets from Secret Manager
    django_settings = get_secret("django_settings")
    env.read_env(io.StringIO(django_settings))
else:
    # Load environment variables from .env file in local development
    env.read_env(os.path.join(BASE_DIR, '.env'))
    MEDIA_URL = '/media/'
    print ("it doesnt think its in prod!")

# Now use the environment variables in settings
SECRET_KEY = env('SECRET_KEY', default="default-secret-key")
DEBUG = env.bool('DEBUG', default=not IS_PRODUCTION)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1', 'portfolio-service-670894227736.europe-west1.run.app'])

DATABASES = {
    'default': env.db(),  # Automatically configures DATABASE_URL
}

# GS_BUCKET_NAME = env('GS_BUCKET_NAME', default=None)

# if GS_BUCKET_NAME:
#     DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
#     MEDIA_URL = f"https://storage.googleapis.com/{GS_BUCKET_NAME}/"
# else:
#     MEDIA_URL = '/media/'

CSRF_TRUSTED_ORIGINS = [
    'https://8001-cs-109655276627-default.cs-europe-west4-bhnf.cloudshell.dev',
    'https://portfolio-service-670894227736.europe-west1.run.app'
]
# Application definition

INSTALLED_APPS = [
    "pages.apps.PagesConfig",
    "projects.apps.ProjectsConfig",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [
            BASE_DIR / "templates/",
        ],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
