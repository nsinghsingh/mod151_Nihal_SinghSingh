from django.shortcuts import render
from .models import Story
from login.models import User

# Create your views here.


def check(request):
    return render(request, 'login.html', {
        'error_message': "Please login",
        'hasAccount': 1
    })


def browse(request):
    if request.session.get('IsLoggedIn', False):
        stories = Story.objects.all()
        return render(request, 'browse.html', {
            "stories": stories
        })
    else:
        return check(request)


def write(request):
    if request.session.get('IsLoggedIn', False):
        return render(request, 'write.html')
    else:
        return check(request)


def submit(request):
    if request.session.get('IsLoggedIn', False):
        title = request.POST['title']
        category = request.POST['category']
        story = request.POST['story']
        user = User.objects.get(username=request.session['username'])
        new_entry = Story(title=title, category= category, story=story, fk_user=user)
        new_entry.save()
        return render(request, 'read.html', {
            'title': title,
            'story': story,
        })
    else:
        return check(request)


def search(request):
    if request.session.get('IsLoggedIn', False): #TO DO
        stories = Story.objects.filter(title__contains=request.POST['story_name'])
        return render(request, 'browse.html', {
            "stories": stories
        })
    else:
        return check(request)


def read(request, id):
    if request.session.get('IsLoggedIn', False): #TO DO
        story = Story.objects.get(id=id)
        return render(request, 'read.html', {
            'title': story.title,
            'story': story.story,
        })
    else:
        return check(request)
