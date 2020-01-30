from django.shortcuts import render
from .models import Story, Extension
from login.models import User
from django.db.models import Q

# Create your views here.


def check(request):
    return render(request, 'login.html', {
        'error_message': "Please login",
        'hasAccount': 1
    })


def browse(request):
    if request.session.get('IsLoggedIn', False):
        stories = Story.objects.filter(is_beginning=True)
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
        new_entry = Story(title=title, category=category, story=story, fk_user=user, is_beginning=True)
        new_entry.save()
        return read(request, new_entry.pk)
    else:
        return check(request)


def search(request):
    if request.session.get('IsLoggedIn', False):
        stories = Story.objects.filter(
            Q(is_beginning=True),
            Q(title__icontains=request.POST['story_name']) | Q(category__iexact=request.POST['story_name'])
        )
        return render(request, 'browse.html', {
            "stories": stories
        })
    else:
        return check(request)


def read(request, id_number):
    if request.session.get('IsLoggedIn', False):
        story = Story.objects.get(id=id_number)
        extensions = Extension.objects.filter(fk_origin=story)
        return render(request, 'read.html', {
            'title': story.title,
            'story': story.story,
            'id': id_number,
            'extensions': extensions,
        })
    else:
        return check(request)


def extend(request, id_number):
    if request.session.get('IsLoggedIn', False):
        story = Story.objects.get(id=id_number)
        return render(request, 'extend.html', {
            'story_id': id_number,
            'title': story.title,
        })
    else:
        return check(request)


def add(request):
    if request.session.get('IsLoggedIn', False):
        title = request.POST['link_title']
        old_story = Story.objects.get(id=request.POST['id_story'].split(':')[0])
        category = old_story.category
        story = request.POST['story']
        user = User.objects.get(username=request.session['username'])
        new_story = Story(title=title, category=category, story=story, fk_user=user, is_beginning=False)
        new_story.save()
        new_entry = Extension(fk_origin=old_story, fk_continuation=new_story)
        new_entry.save()
        return read(request, new_story.pk)
    else:
        return check(request)


def mystories(request):
    if request.session.get('IsLoggedIn', False):
        stories = Story.objects.filter(fk_user__username=request.session['username']).order_by('title')
        return render(request, 'mystories.html', {
            "stories": stories
        })
    else:
        return check(request)


def change(request):
    if request.session.get('IsLoggedIn', False):
        old_story = Story.objects.get(id=request.POST['old_title'].split('.')[0])
        if len(request.POST['title']) > 0:
            old_story.title = request.POST['title']
        if len(request.POST['category']) > 0:
            old_story.category = request.POST['category']
        if len(request.POST['story']) > 0:
            old_story.story = request.POST['story']
        old_story.save()
        return mystories(request)
    else:
        return check(request)


def delete(request, id_number):
    if request.session.get('IsLoggedIn', False):
        story = Story.objects.get(id=id_number)
        story.delete()
        return mystories(request)
    else:
        return check(request)
