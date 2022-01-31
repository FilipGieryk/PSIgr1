from email import message
from msilib.schema import CustomAction
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User, FriendRequest
from .forms import UserCreateForm
from django.shortcuts import render
from django.http import HttpResponse
import random


def chat(request):
    return render(request, 'base/chat.html')
def room(request, room_name):
    return render(request, 'base/room.html', {
        'room_name': room_name
    })
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    items = list(User.objects.all())
    randomize= random.choice(items)
    cnt = 0
    no_friends = False
    while(randomize == request.user or randomize in User.objects.filter(user=request.user).filter(username=randomize.username) or FriendRequest.objects.filter(from_user = request.user,to_user= randomize)) and cnt<10:
        randomize = random.choice(items)
        cnt+=1
    if cnt>= 10:
        randomize = request.user
        no_friends = True
    context = {'randomize': randomize,'no_friends': no_friends}
    return render(request, 'base/home.html', context)




def userProfile(request, pk):
    user = User.objects.get(id=pk)
    context ={user: 'user'}
    user = User.objects.get(id=pk)

    context= {'user':user}
    return render(request, 'base/profile.html', context)


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "user does not exist")

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = UserCreateForm()

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})



def removefriend(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method =='POST':
        friendusername=request.POST.get('friendusername')
        friend = User.objects.get(username=friendusername)
        user = request.user
        
        if friendusername in User.objects.filter(user=user).filter(user=friend):
            return redirect('friends')
        user.friends.remove(friend)
        friend.friends.remove(user)
    return redirect('/friends')


def addfriend(request,pk):
    if not request.user.is_authenticated:
        return redirect('login')
    from_user=request.user
    to_user = User.objects.get(id=pk)
    frequest, created=FriendRequest.objects.get_or_create(from_user=from_user,to_user=to_user)
    return redirect('home')

def accept_request(request, pk):
    frequest = FriendRequest.objects.get(id=pk)
    user1 = request.user
    user2 = frequest.from_user
    user1.friends.add(user2)
    user2.friends.add(user1)
    FriendRequest.objects.get(id=pk).delete()
    return redirect('friends')
  

def friends(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method=='POST':
        friend=request.POST.get('friendusername')
        from_user=request.user
        to_user = User.objects.get(username=friend)
        if from_user==to_user:
            return HttpResponse("cannot add yourself") 
        if User.objects.filter(friends=to_user).exists():
            return redirect('friends')
        if User.objects.filter(username = to_user.username).exists()==False:
            return HttpResponse('no such user')
        if friend =="":
            return redirect('friends') 
        frequest, created=FriendRequest.objects.get_or_create(from_user=from_user,to_user=to_user)
    fr = FriendRequest.objects.filter(to_user=request.user)
    unsorted_friends=User.objects.all().filter(user=request.user.id)
    user_friends=sorted(list(unsorted_friends.values()),key=lambda k:k['username'])
    context = {'user_friends': user_friends, 'fr':fr}
    return render(request,'base/friends.html',context)


def checkview(request):
    if request.user.is_anonymous or request.user.is_active==False:
        return redirect('/accounts/login')
    if request.method == 'POST':
        user = request.user 
        friendusername =request.POST.get("friendusername")
        friend = User.objects.get(username=friendusername)
        if request.user.username==friendusername:
            return redirect('friends')
        if friend in User.objects.filter(user=user):
            return redirect('/room/'+friendusername)
        else:
            return redirect('user-profile')
    
    return redirect('user-profile')

