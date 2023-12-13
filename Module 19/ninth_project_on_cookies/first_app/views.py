from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
# Create your views here.


def home(requrest):
    response = render(requrest, 'home.html')
    response.set_cookie('name', 'rahim')
    # response.set_cookie('name', 'karim', max_age=3)
    # response.set_cookie('name', 'karim', expires=datetime.now() + timedelta(days=3))
    response.set_cookie('name', 'karim', expires=datetime.utcnow() + timedelta(days=3))
    return response


def get_cookie(request):
    name = request.COOKIES.get('name')
    return render(request, 'get_cookie.html', {'name': name})

def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')
    return response


# session vs cookie
# 1. session is a temporary storage
# 2. cookie is a permanent storage

def set_session(request):
    # request.session['name'] = 'rahim'
    data = {
        'name': 'rahim',
        'age': 25,
        'language': 'Bangla',
    }
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    request.session.update(data)
    return render(request, 'home.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name')
        age = request.session.get('age')
        language = request.session.get('language')
        request.session.modified = True
        return render(request, 'get_session.html', {'name': name, 'age': age, 'language': language})
    else:
        return HttpResponse('no session found. kindly login again')


def delete_session(request):
    # del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'delete_session.html')