from django.shortcuts import render, get_object_or_404
from app.models import Profile, Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import string
import random

@login_required
def newsfeed(request):
    if (request.GET.get('q', '') == ''):
        profiles = Profile.objects.filter(active=True)
    else:
        profiles = Profile.objects.filter(interests__icontains=request.GET.get('q', ''))
    return render(request, 'app/newsfeed.html', {'profiles': profiles})
 
@login_required 
def profile(request, slug):
    user = get_object_or_404(User, username=slug)
    return render(request, 'app/profile.html', {'profile': user.get_profile(), 'user': user})

def index(request):
    return render(request, 'app/index.html', {})

def loginview(request):
    return render(request, 'app/loginview.html', {})    

@login_required
def home(request):
    return render(request, 'app/home.html', {})  

@login_required
def question(request):
    questions = Question.objects.all()
    return render(request, 'app/question.html', {'questions': questions})

@login_required
def questionsubmit(request):
    body = request.POST['body']
    slug = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))
    Question.objects.create(body = body, slug = slug, username = request.user.username);
    return HttpResponseRedirect('../question') 

@login_required
def answersubmit(request):
    body = request.POST['body']
    question = request.POST['question']
    Answer.objects.create(body = body, question = question, username = request.user.username);
    return HttpResponseRedirect('../answer?q=' + question)                       
    
@login_required 
def answer(request):
    question = get_object_or_404(Question, slug=request.GET.get('q', ''))
    answers = Answer.objects.filter(question__icontains=request.GET.get('q', ''))
    return render(request, 'app/answer.html', {'answers': answers, 'question' : question})

def register(request):
    return render(request, 'app/register.html', {})
	
def registersubmit(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    return HttpResponse("%s %s" % (username, email))
    User.objects.create_user(username=username, email=email, password=password, last_name='', first_name='')
    return HttpResponseRedirect('/home')	    

def deauthorize(request):
    logout(request)
    return HttpResponseRedirect('../')			


def authorize(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
			login(request, user)
			return HttpResponseRedirect('../newsfeed')			
        else:
            print('account disabled, sorry!')
    else:
        print('oops, wrong login')
        return HttpResponseRedirect('../')			

@login_required
def edit(request):
        return render(request,'app/edit.html',{'user': request.user, 'profile': request.user.get_profile()})        
