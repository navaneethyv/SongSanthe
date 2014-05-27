import os

from django.core.urlresolvers import reverse_lazy


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

# print PACKAGE_ROOT

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = [
    # ("Your Name", "your_email@example.com"),
]

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "devel.db",
    }
}

DEFAULT_DOMAIN = 'songsanthe.com'


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "UTC"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/site_media/static/"

STATIC_FILES = os.path.join(PACKAGE_ROOT, "static")

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(PACKAGE_ROOT, "static"),
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = "lelsy6zfr@oc735y(5$&76d6wfh&s0d=__yf9fhu04%f+pxjhk"


MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "account.context_processors.account",
    "pinax_theme_bootstrap.context_processors.theme",
    "social_auth.context_processors.social_auth_by_name_backends",
    "social.friends.context_processors.suggestions"
]


MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "social_auth.middleware.SocialAuthExceptionMiddleware"
]

ROOT_URLCONF = "social.urls"

# Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = "social.wsgi.application"

TEMPLATE_DIRS = [
    os.path.join(PACKAGE_ROOT, "templates"),
    os.path.join(PACKAGE_ROOT, "templates/profile")
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    #activities -- see the source kid!
    'actstream',
    
    # theme
    "pinax_theme_bootstrap",
    "django_forms_bootstrap",
    
    # external
    "account",
    "metron",
    "social_auth",
    "djcelery",
    "south",

    #avatar
    "avatar",
        
    #db-schema
    "django_extensions",
    
    # project
    "social",
    "social.friends",
    "social.profiles",
    "social.content",
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False
ACCOUNT_LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
LOGIN_URL = reverse_lazy("account_login_signup")
LOGIN_REDIRECT_URL = '/home'
# reverse_lazy("home")

# Social Auth

LOGIN_ERROR_URL = "/account/social/connections/"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "social_auth.backends.twitter.TwitterBackend",
    "social_auth.backends.facebook.FacebookBackend",
    "social_auth.backends.google.GoogleOAuth2Backend",
]

SOCIAL_AUTH_ASSOCIATE_BY_MAIL = False

SOCIAL_AUTH_PIPELINE = [
    "social.pipeline.prevent_duplicates",
    
    "social_auth.backends.pipeline.social.social_auth_user",
    "social_auth.backends.pipeline.user.get_username",
    "social_auth.backends.pipeline.user.create_user",
    "social_auth.backends.pipeline.social.associate_user",
    "social_auth.backends.pipeline.social.load_extra_data",
    "social_auth.backends.pipeline.user.update_user_details",
    
    "social.pipeline.import_friends"
]

GOOGLE_OAUTH2_CLIENT_ID = os.environ.get("GOOGLE_OAUTH2_CLIENT_ID", "")
GOOGLE_OAUTH2_CLIENT_SECRET = os.environ.get("GOOGLE_OAUTH2_CLIENT_SECRET", "")

TWITTER_CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY", "")
TWITTER_CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET", "")

FACEBOOK_APP_ID = os.environ.get("FACEBOOK_APP_ID", "632435750126361")
FACEBOOK_API_SECRET = os.environ.get("FACEBOOK_API_SECRET", "")
FACEBOOK_EXTENDED_PERMISSIONS = [
    "email",
]

GOOGLE_OAUTH_EXTRA_SCOPE = [
    "https://www.googleapis.com/auth/plus.login",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]

GOOGLE_OAUTH2_EXTRA_DATA = [
    ("given_name", "first_name"),
    ("family_name", "last_name"),
    ("email", "email"),
]

FACEBOOK_EXTRA_DATA = [
    ("first_name", "first_name"),
    ("last_name", "last_name"),
]

TWITTER_EXTRA_DATA = [
    ("name", "name"),
    ("screen_name", "screen_name"),
    ("profile_image_url", "profile_image_url"),
]


# Activity Stream
ACTSTREAM_SETTINGS = {
    'MODELS': ('auth.user', 'content.Content', 'sites.site','content.Music','content.Lyrics','content.Upvoters'),
    # 'MANAGER': 'myapp.streams.MyActionManager',
    'FETCH_RELATIONS': True,
    'USE_PREFETCH': True,
    'USE_JSONFIELD': True,
    'GFK_FETCH_DEPTH': 1,
}



# Celery

BROKER_TRANSPORT = "redis"
BROKER_HOST = "localhost"
BROKER_PORT = 6379
BROKER_VHOST = "0"
BROKER_PASSWORD = ""
BROKER_POOL_LIMIT = 10

CELERY_RESULT_BACKEND = "redis"
CELERY_REDIS_HOST = "localhost"
CELERY_REDIS_PORT = 6379
CELERY_REDIS_PASSWORD = ""
CELERY_ALWAYS_EAGER = True
CELERYD_HIJACK_ROOT_LOGGER = False
CELERYD_LOG_LEVEL = "INFO"
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_IGNORE_RESULT = True
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERY_DISABLE_RATE_LIMITS = True
CELERY_TASK_PUBLISH_RETRY = True
CELERY_TASK_RESULT_EXPIRES = 7 * 24 * 60 * 60  # 7 Days
CELERYD_TASK_TIME_LIMIT = 120
CELERYD_TASK_SOFT_TIME_LIMIT = 120
#CELERY_IMPORTS=("tasks",)
