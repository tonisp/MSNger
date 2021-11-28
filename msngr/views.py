from django.shortcuts import render, redirect
from . models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

'''
from logging import getLogger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

LOGGER = getLogger()

@login_required
def loggedinuser(request):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html'), {
        'username': username,
        'room': room,
        'room_details': room_details
    })
'''


def home(request):
    return render(request, 'home.html')

@login_required
def room(request, room):
    username = request.user.username
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
        })


def checkview(request):
    room = request.POST['room_name']
    username = request.user.username

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    user_profile = request.user.profile
    room_id = request.POST['room_id']
    room = Room.objects.get(id = room_id)
    new_message = Message.objects.create(value=message, user=user_profile, room=room)
    return HttpResponse('Message sent successfully')

def getMessages(request, room_id):
    room = Room.objects.get(id=room_id)

    messages = Message.objects.filter(room=room)
    messages_response = []

    active_users = []

    for x in messages:
        json_msg = {'user':x.user.user.username, 'message':x.value, 'datetime':x.date}
        messages_response.append(json_msg)

    for x in room.users.all():
        json_msg = {'user':x.user.username}
        active_users.append(json_msg)

    return JsonResponse({"messages":messages_response, "active_users":active_users})

@login_required
def users(request):
    return render(request, 'users.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, name='registered_room')
        else:
            messages.success(request, ("Login failed"))
    else:
        return render(request, 'login.html', {})




#def registered_room(request):
   # return render(request, room == 'registered')