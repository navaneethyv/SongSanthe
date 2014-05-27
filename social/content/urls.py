from django.conf.urls import patterns, url

from .views import upload_lyrics, upload_music
from .views import show_lyrics, show_music

from .views import (
    upvote,
    downvote,
    undo_upvote,
    undo_downvote,
    )

urlpatterns = patterns(
    "",
    # url(r"^$", home, name="myhome"),
    url(r"^lyrics", upload_lyrics, name='upload_lyrics'),
    url(r"^music", upload_music, name='upload_music'),
    url(r"^show_lyrics/(?P<content_pk>\d+)/",show_lyrics,name='show_lyrics'),
    url(r"^show_music/(?P<content_pk>\d+)/",show_music,name='show_lyrics'),

    url(r"^upvote/(?P<content_pk>\d+)/",upvote,name='upvote'),
    url(r"^downvote/(?P<content_pk>\d+)/",downvote,name='downvote'),
    url(r"^undo_upvote/(?P<content_pk>\d+)/",undo_upvote,name='undo_upvote'),
    url(r"^undo_downvote/(?P<content_pk>\d+)/",undo_downvote,name='undo_downvote'),

    # url(r"share_lyrics", share_lyrics, name='lyrics'),

)
