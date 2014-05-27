from django.contrib.auth.models import User

from celery.task import Task
from social_auth.models import UserSocialAuth

from .friends.models import Suggestion
from .social import Provider


class ProcessSocialNetwork(Task):
    
    def run(self, user_pk, provider):
        print "Running Friend import Tasks"
        user = User.objects.get(pk=user_pk) # get song santhe regestered user
        print "For",
        print user
        social = Provider(user, provider)   # get a reference to that persons social account (fb/twitter/google)
        total = 0
        
        for friend in social.friends():
            #getting his friends who use songsanthe
            social_auth = UserSocialAuth.get_social_auth(
                provider=provider,
                uid=friend["id"]
            )   
            if social_auth is not None:
                Suggestion.objects.create_suggestions(user, social_auth.user)
            total += 1

        #stupid suggestions generater

        strangers = User.objects.exclude(pk=user_pk)
        for stranger in strangers:
            print "The users and the strangers per iterations "
            print user,stranger
            suggested =  Suggestion.objects.create_suggestions(user,stranger)
            total +=1
        return total
