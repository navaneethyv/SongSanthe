from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    "",
    url(r"^activity/", include("actstream.urls")),
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^home/",include("social.profiles.urls")),
    url(r"^upload/",include("social.content.urls")),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^friends/", include("social.friends.urls")),

    #user activity stuff
    url(r"^activity/", include("actstream.urls")),
    
    url(
        r"^account/social/connections/$",
        TemplateView.as_view(template_name="account/connections.html"),
        name="account_social_connections"
    ),
    url(r"^account/social/", include("social_auth.urls")),
    url(
        r"^account/login/$",
        TemplateView.as_view(template_name="account/signup.html"),
        name="account_login"
    ),
    url(
        r"^account/signup/$",
        TemplateView.as_view(template_name="account/signup.html"),
        name="account_signup"
    ),
    url(r"^account/", include("account.urls")),

    #avatar
    url(r'^avatar/', include('avatar.urls')),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
