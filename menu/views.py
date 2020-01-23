from django.shortcuts import render

# Create your views here.


def check(request):
    return render(request, 'login.html', {
        'error_message': "Please login",
        'hasAccount': 1
    })


def browse(request):
    if request.session.get('IsLoggedIn', False):
        return render(request, 'browse.html')
    else:
        return check(request)

