from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# your views here.


def login(request):
    if request.session.has_key('user_in'):
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username == 'user' and password == '12345':
                request.session['user_in'] = 'user_in'
                return redirect('home')
            else:
                return redirect('login')
        else:
            return render(request, 'login.html')


def home(request):
    if request.session.has_key('user_in'):
        return render(request, 'home.html')
    else:
        return redirect('login')

def logout(request):
    request.session.flush()
    return redirect('login')
   