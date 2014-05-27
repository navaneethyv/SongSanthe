from django.contrib import admin
from .models import Content,Music,Lyrics,Tag

admin.site.register(Content)
admin.site.register(Music)
admin.site.register(Lyrics)
admin.site.register(Tag)