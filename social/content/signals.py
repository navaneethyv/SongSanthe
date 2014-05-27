#Use if needed!
from django.db.models.signals import post_save
from actstream import action
from .models import Content, Upvoters

def add_content(sender, instance, created, **kwargs):
    action.send(instance, verb='content created')


def up_voted(sender, instance, created, **kwargs):
    action.send(instance, verb='upvoted')


post_save.connect(add_content, sender=Content)

post_save.connect(up_voted, sender=Upvoters)