import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from .models import Tweet, Comment, Mark


@csrf_exempt
def create_tweet(request):
    if request.method == 'POST':
        # title = request.POST.get('title')
        # body = request.POST.get('body')
        # author = request.POST.get('author')
        data = json.loads(request.body)
        # Tweet.objects.create(title=data['title'])
        new_tweet = Tweet.objects.create(**data)
        json_data = {
            'title': new_tweet.title,
            'body': new_tweet.body,
            'author': new_tweet.author
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        tweets = Tweet.objects.all()
        data = []
        for tweet in tweets:
            data.append(
                {
                    'title': tweet.title,
                    'body': tweet.body,
                    'author': tweet.author
                }
            )
        json_data = json.dumps(data)
        # return HttpResponse(json_data)
        return JsonResponse(json_data, safe=False)


@csrf_exempt
def create_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_tweet = Comment.objects.create(**data)
        json_data = {
            'title': new_tweet.title,
            'text': new_tweet.text,
            'tweet': new_tweet.tweet.id
        }
        print(json_data)
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        tweets = Comment.objects.all()
        data = []
        for tweet in tweets:
            data.append(
                {
                    'title': tweet.title,
                    'text': tweet.text,
                    'tweet': tweet.tweet.id
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)


@csrf_exempt
def create_mark(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_tweet = Mark.objects.create(**data)
        json_data = {
            'mark_value': new_tweet.mark_value,
            'tweet': new_tweet.tweet.id
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        tweets = Mark.objects.all()
        data = []
        for tweet in tweets:
            data.append(
                {
                    'mark_value': tweet.mark_value,
                    'tweet': tweet.tweet.id
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)

