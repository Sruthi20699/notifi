from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from myapp.models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def Home(request):
    return render(request, "index.html", {'user': request.user})


def adninlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('new_page')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('adminlogin')
    return render(request, 'adminlogin.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('new_page')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Taken')
                return redirect('login')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                auth.login(request, user)  # Log in the user after registration
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    return render(request, 'register.html')

def new_page(request):
    return render(request, 'new_page.html')

def logout_view(request):
    auth.logout(request)
    return redirect('/')

def admin_view(request):
    x=User.objects.all()
    return render(request,'adminhome.html',{'data':x})


def create_message(request):
    new_message = Message.objects.create(sender=sender, recipient=recipient, message_text=message_text)
    send_notification(new_message.sender, new_message.recipient, new_message.message_text)


def send_notification(sender, recipient, message_text):
    channel_layer = get_channel_layer()

    notification_data = {
        'type' : 'send_notification', 
        'sender_id' : sender.id,
        'recipient_id' : recipient.id,
        'message' : message_text,

    }

    async_to_sync(channel_layer.group_send)(
        f"notifications_{recipient.id}",
        notification_data
    )