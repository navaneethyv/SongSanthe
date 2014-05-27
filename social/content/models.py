from django.db import models

from social.settings import MEDIA_ROOT

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from avatar.util import get_username , force_bytes, invalidate_cache  #DRY

import hashlib
# Create your models here.


# Store music here

def music_store_path(instance,filename):
    print 'getting path'
    tmppath = MEDIA_ROOT+'/music/'+ get_username(instance.content.user)
    #avoid conflicting file names
    new_name = hashlib.md5(filename).hexdigest()+".mp3"
    save_to = tmppath+"/"+new_name
    print save_to
    return save_to


content_type_choices = (
                ('MUSIC','music'),
                ('LYRICS','lyrics'),
        )

class Content(models.Model):
    """class to maintain the content uploaded by the user"""

    user = models.ForeignKey(User, related_name="content_uploader") #one who uploads
    time_stamp = models.DateTimeField(auto_now=True)
    content_type = models.TextField(choices=content_type_choices,default='LYRICS')
    user_content_id = models.IntegerField(null=True, blank=True )  #?


class Music(models.Model):
    """docstring for music"""
    content = models.OneToOneField(Content)
    title = models.TextField()
    comment = models.TextField(null=True, blank=True )
    filepath = models.TextField()
    file_store_to = models.FileField(upload_to=music_store_path)

class Lyrics(models.Model):
    content = models.OneToOneField(Content)
    lyrics_title = models.TextField()
    lyrics_content = models.TextField()


class Tag(models.Model):
    content = models.ForeignKey(Content) # Not unique coz of storing many !!    
    tag_name = models.TextField()


class Upvoters(models.Model):

    """Voters list"""
    """Must add upvoters to this list as soon as new vote is added"""
    content = models.ForeignKey(Content)
    user = models.ForeignKey(User,related_name='upvoter')

class Downvoters(models.Model):

    """Voters list"""
    """Must add down voters to this list as soon as new vote is added"""
    content = models.ForeignKey(Content)
    user = models.ForeignKey(User,related_name='downvoter')