
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string

from account.decorators import login_required

from actstream.models import ( actor_stream,
    user_stream,
    followers,
    following
    )


from django.contrib.auth.models import User
from social.content.models import Content,Lyrics,Music,Tag, Upvoters, Downvoters


@login_required
def home(request):
    return render(request,'profile/home.html')

def share_music(request):
    return render(request,'profile/put_music.html')


def share_lyrics(request):
    return render(request,'profile/put_lyrics.html')

@login_required
def my_activities(request):
    my_activity = actor_stream(request.user) 
    print my_activity
    activity_set = []
    for that_action in my_activity:
        target = that_action.target

        if isinstance(that_action.target,User):
            target_url = "/home/user/"+str(that_action.target.id )
        if isinstance(that_action.target,Content):
            if that_action.target.content_type == "MUSIC":
                target = that_action.target.music.title
                target_url = "/upload/show_music/"+str(that_action.target.pk)+" "
            else:
                if that_action.target.content_type == "LYRICS":
                    target = that_action.target.lyrics.lyrics_title                    
                    target_url = "/upload/show_lyrics/"+str(that_action.target.pk)
        activity_set.append({'actor':that_action.actor.first_name, 'target':target,'target_url':target_url,"verb":that_action.verb,
            "timesince":that_action.timesince, "action_object":that_action.action_object})
    
    ctx = {
        "activity_set": activity_set, 
    }
    return render(request, "profile/my_activities.html", ctx)
    # my_actions = format_activity(request.user)


@login_required
def my_stream(request):

    """ Activities of the ones i follow """
    my_activity = user_stream(request.user) 
    print my_activity
    activity_set = []
    for that_action in my_activity:
        target = that_action.target
        actor_url = "#"
        actor_url = "/home/user/"+str(that_action.actor.id)

        if isinstance(that_action.target,User):
            target_url = "/home/user/"+str(that_action.target.id )
        if isinstance(that_action.target,Content):
            if that_action.target.content_type == "MUSIC":
                target_url = "/upload/show_music/"+str(that_action.target.pk)+" "
                target = that_action.target.music.title
            else:
                if that_action.target.content_type == "LYRICS":
                    target_url = "/upload/show_lyrics/"+str(that_action.target.pk)
                    target = that_action.target.lyrics.lyrics_title
        activity_set.append({'actor':that_action.actor.first_name, 'actor_url':actor_url, 'target':target,'target_url':target_url,"verb":that_action.verb,
            "timesince":that_action.timesince, "action_object":that_action.action_object})
    
    ctx = {
        "activity_set": activity_set, 
    }
    return render(request, "profile/home.html", ctx)

@login_required
def user_activities(request,user_pk):
    """ Display all of his activities """

    my_activity = user_stream(User.objects.get(pk=user_pk))
    print my_activity
    cur_user = User.objects.get(pk=user_pk)
    print cur_user.first_name
    activity_set = []
    for that_action in my_activity:
        target = that_action.target
        actor_url = "#"
        actor_url = "/home/user/"+str(that_action.actor.id)

        if isinstance(that_action.target,User):
            target_url = "/home/user/"+str(that_action.target.id )
        if isinstance(that_action.target,Content):
            if that_action.target.content_type == "MUSIC":
                target_url = "/upload/show_music/"+str(that_action.target.pk)+" "
                target = that_action.target.music.title
            else:
                if that_action.target.content_type == "LYRICS":
                    target_url = "/upload/show_lyrics/"+str(that_action.target.pk)
                    target = that_action.target.lyrics.lyrics_title
        activity_set.append({'actor':that_action.actor.first_name,'actor_url':actor_url, 'target':target,'target_url':target_url,"verb":that_action.verb,
            "timesince":that_action.timesince, "action_object":that_action.action_object})
    
    
    ctx = {
        "activity_set": activity_set, 
        'cur_user':cur_user,
    }
    return render(request, "profile/user_activities.html", ctx)

@login_required
def get_following_list(request,user_pk):
    """List of users followed by user_pk"""
    connection = User.objects.get(pk=user_pk)
    node = request.user
    connection_follows = following(User.objects.get(pk=user_pk))
    node_follows = following(node)
    following_list = []
    for connected in connection_follows:
        if connected in node_follows:
            following_list.append({"followed_by_connection":connected, "followed_by_me":"Following"})
        else:
            following_list.append({"followed_by_connection":connected, "followed_by_me":"Not Following"})
    is_cur_user = False
    if (request.user == connection):
        is_cur_user = True


    ctx = {
        "following_list": following_list, 
        "is_cur_user" : is_cur_user,
        "connection" : connection.first_name,
        "cur_user" : connection,
    }

    print 'following'
    print following_list
    return render(request,"profile/user_connections.html",ctx)

@login_required
def get_followers_list(request,user_pk):
    """List of users who follow  user_pk"""
    print "getting  followers_list"
    connection = User.objects.get(pk=user_pk)
    cur_user = connection
    node = request.user
    followers_of_user = followers(User.objects.get(pk=user_pk))
    node_follows = following(node)
    followers_list = []
    for connected in followers_of_user:
        if connected in node_follows:
            followers_list.append({"followed_by_connection":connected, "followed_by_me":"Following"})
        else:
            followers_list.append({"followed_by_connection":connected, "followed_by_me":"Not Following"})

    is_cur_user = False
    if  request.user == connection:
        is_cur_user = True

    ctx = {
        "followers_list": followers_list, 
        'cur_user':cur_user,
        'followed_user' : connection.first_name,
        'is_cur_user' :  is_cur_user,
    }

    print 'followers'
    print followers_list
    return render(request,"profile/user_connections.html",ctx)
