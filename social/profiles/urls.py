from django.conf.urls import patterns, url
from .views import  (share_music, 
    share_lyrics, 
    my_activities,
    my_stream, 
    user_activities, 
    get_followers_list,
    get_following_list,
    )


urlpatterns = patterns(
    "",
    url(r"^$", my_stream, name="home"),
    url(r"share_music", share_music, name='music'),
    url(r"share_lyrics", share_lyrics, name='lyrics'),
    url(r"self_feeds",my_activities,name='my_activities'),
    url(r"user/(?P<user_pk>\d+)/",user_activities,name='user_activities'),
    url(r"followers/(?P<user_pk>\d+)/",get_followers_list, name='followers_list'),
    url(r"following/(?P<user_pk>\d+)/",get_following_list, name='following_list'),


)
