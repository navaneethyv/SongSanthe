# Create your views here.
import json
from django.contrib import messages
from social.content.models import Content,Lyrics,Music,Tag, Upvoters, Downvoters
from django.contrib.auth.models import User


from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string

from account.decorators import login_required

from actstream import action

@login_required

def upload_lyrics(request):
    if request.method == 'POST':
        try:
            new_content = Content()
            new_content.user = request.user
            new_content.content_type = 'LYRICS'
            new_content.save()
            print new_content.id

        except Exception as E :
            print "failed to create content for lyrics"
            print E.message
        # Now save the lyrics in a linked lyrics object
        try:
            new_lyrics = Lyrics()
            new_lyrics.content = new_content
            new_lyrics.lyrics_title = request.POST['title']
            new_lyrics.lyrics_content = request.POST['lyrics_content']
            new_lyrics.save()
            
            # This is an activity, people should know it!
            action.send(request.user, verb='uploaded lyrics to',target=new_content)

        except Exception as E :
            print "failed to Save lyrics"
            print E.message
            return HttpResponse("Well this is embarrasing!") 
        messages.add_message(request, messages.INFO, 'Lyrics Uploaded!')
        return render_to_response("profile/home.html",
        context_instance=RequestContext(request))
        # return HttpResponse("<html><body><pre>"+new_lyrics.lyrics_content+"<pre></body></html>")    
    else :
        return HttpResponse("Yeah This won't work :p")

@login_required
def upload_music(request):
    if request.method == 'POST':
        try:
            new_content = Content()
            new_content.user = request.user
            new_content.content_type = 'MUSIC'
            new_content.save()

        except Exception as E :
            print "failed to create content for music"
            print E.message
        # Now save the lyrics in a linked lyrics object
        try:
            new_music = Music()
            new_music.content = new_content
            new_music.title = request.POST['music_title']
            new_music.comment = request.POST['music_comments']
            new_music.file_store_to = request.FILES['music_file']
            new_music.save()
            print new_music.id
            print new_music

            # This is an activity, people should know it!
            action.send(request.user, verb='uploaded music to',target=new_content)

        except Exception as E :
            print "failed to Save music"
            print E.message
            return HttpResponse("Well this is embarrasing!") 
        messages.add_message(request, messages.INFO, 'Music Uploaded!')
        return render_to_response("profile/home.html",
        context_instance=RequestContext(request))
        # return HttpResponse("<html><body><pre>"+new_lyrics.lyrics_content+"<pre></body></html>")    
    else :
        return HttpResponse("Yeah This won't work :p")

def converter(votes):
    if votes > 1000:
        votes = (votes/1000)
    return str(votes)


@login_required
def show_lyrics(request,content_pk):
    lyrics_container = Content.objects.get(pk=content_pk)
    lyrics_object = lyrics_container.lyrics

    votes = Upvoters.objects.filter(content=lyrics_container).count()
    votes = converter(votes)

    rendered_lyrics = {
        "lyrics_title": lyrics_object.lyrics_title,
        "lyrics_content": lyrics_object.lyrics_content,
        "lyrics_auther": lyrics_container.user.first_name,
        "content_pk": content_pk,
        'upvote_count': votes
    }
    return render(request, "content/show_lyrics.html", rendered_lyrics)


@login_required
def show_music(request,content_pk):
    music_container = Content.objects.get(pk=content_pk)
    music_object = music_container.music
    storer = str(music_object.file_store_to)
    print storer
    votes = Upvoters.objects.filter(content=music_container).count()
    votes = converter(votes)

    path_here = storer.split("social")
    print path_here
    rendered_lyrics = {
        "music_title": music_object.title,
        "music_comment": music_object.comment,
        "music_auther": music_container.user.first_name,
        "content_pk": content_pk,
        "file_path" : path_here[1],
        'upvote_count': votes
    }
    return render(request, "content/show_music.html", rendered_lyrics)




@login_required
def upvote(request,content_pk):
    cancelled_upvote = False
    new_vote = Upvoters()
    content = Content.objects.get(pk=content_pk)
    voters_till_now = Upvoters.objects.filter(content=content)
    if content.user != request.user :
        for voter in voters_till_now:
            if voter.user == request.user:
                voter.delete()
                print 'undo upvote'
                cancelled_upvote = True
                break
        if not cancelled_upvote:
            new_vote.content = content
            new_vote.user =  request.user
            new_vote.save()
            print 'new upvote'
            action.send(request.user,verb='upvoted',target=content)
        status = not cancelled_upvote
        return HttpResponse(json.dumps({"status": str(status) }), content_type="application/json")
    else:
        print "self vote??!!, That ain't happeneing "
        return HttpResponse(json.dumps({"status": "can't do that!!" }), content_type="application/json")

        # print content_pk 

@login_required
def downvote(request,content_pk):
    cancelled_downvote = False
    new_vote = Downvoters()
    content = Content.objects.get(pk=content_pk)
    voters_till_now = Downvoters.objects.filter(content=content)
    for voter in voters_till_now:
        if voter.user == request.user:
            voter.delete()
            cancelled_vote = True
            print 'undo downvote'
            break
    if not cancelled_downvote:
        new_vote.content = content
        new_vote.user =  request.user
        new_vote.save()
        print 'new downvote'


        # action.send(request.user,verb='downvoted',target=content)
    return HttpResponse(json.dumps({"status": "Successfully Downvoted"}), content_type="application/json")
    # print content_pk 


def undo_upvote(request,content_pk):
    pass

def undo_downvote(request,content_pk):
    pass
