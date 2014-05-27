import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string

from account.decorators import login_required

from .models import Suggestion, Relationship

    

from django.contrib.auth.admin import User
from actstream.actions import follow, unfollow


@login_required
def friends(request):
    ctx = {
        "requests": Relationship.objects.requests_for_user(request.user),
        "pending": Relationship.objects.pending_for_user(request.user),
        "accepted": Relationship.objects.accepted_for_user(request.user),
    }
    return render(request, "friends/friends.html", ctx)


@login_required
def suggestions(request):
    ctx = {
        "suggestions": Suggestion.objects.for_user(request.user)
    }
    # print ctx
    print Suggestion.objects.for_user(request.user)
    return render(request, "friends/suggestions.html", ctx)


@login_required
def ajax_request_suggestion(request, pk):
    suggestion = get_object_or_404(Suggestion, pk=pk, from_user=request.user)
    suggestion.request()
    return HttpResponse(json.dumps({"html": ""}), content_type="application/json")


@login_required
def ajax_ignore_suggestion(request, pk):
    suggestion = get_object_or_404(Suggestion, pk=pk, from_user=request.user)
    suggestion.ignore()
    return HttpResponse(json.dumps({"html": ""}), content_type="application/json")


@login_required
def ajax_accept_request(request, pk):
    relationship = get_object_or_404(Relationship, pk=pk, to_user=request.user)
    relationship.accept()
    ctx = {
        "friend": relationship
    }
    return HttpResponse(json.dumps({
        "html": "",
        "prepend-fragments": {
            ".friends": render_to_string("friends/_request.html", RequestContext(request, ctx)),
        }
    }), content_type="application/json")


@login_required
def ajax_decline_request(request, pk):
    relationship = get_object_or_404(Relationship, pk=pk, to_user=request.user)
    relationship.decline()
    return HttpResponse(json.dumps({"html": ""}), content_type="application/json")


#  enough 
#  Real Stuff is here!!

@login_required
def follow_user(request, user_pk):
    try:

        user_to_follow = User.objects.get(pk=user_pk)
        is_followed = follow(request.user,user_to_follow)
        print is_followed
    except Exception as E:
        print E.message
    return HttpResponse(json.dumps({"follow_status":"Following"}), content_type="application/json")


@login_required
def unfollow_user(request, user_pk):
    try:
        user_to_unfollow = User.objects.get(pk=user_pk)
        is_unfollowed = unfollow(request.user,user_to_unfollow)
        print is_unfollowed
    except Exception as E:
        print E.message
    return HttpResponse(json.dumps({"follow_status":"Not Following"}), content_type="application/json")
