from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as lgout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.management import call_command
from django.shortcuts import render, HttpResponseRedirect
from .models import music
from .forms import EmailForm, UploadForm, UserCreateForm
import pdb

# Create your views here.
@login_required
def index(request):

    #select the latest song sheets
    latest_music_list = music.objects.filter(file_type=1)
    latest_music_list = latest_music_list.order_by('-added')[:3]
    
    #select the latest song books
    latest_book_list = music.objects.filter(file_type=2)
    latest_book_list = latest_book_list.order_by('-added')[:3]
    
    #select the latest teachings
    latest_teaching_list = music.objects.filter(file_type=3)
    #latest_teaching_list = latest_book_list.order_by('-added')[:3]
    
    #create the context variable
    context = {'latest_music_list': latest_music_list,
            'latest_book_list': latest_book_list,
            'latest_teaching_list': latest_teaching_list,
        }
    return render(request, 'DrydenMusicApp/index.html', context)

@login_required    
def sheet_list(request):
    l = music.objects.filter(file_type=1)
    l = l.order_by('title')
    context = {'sheet_list':l}
    return render(request, 'DrydenMusicApp/sheet_list.html', context)

@login_required    
def book_list(request):
    l = music.objects.filter(file_type=2)
    l = l.order_by('title')
    context = {'book_list':l}
    return render(request, 'DrydenMusicApp/book_list.html', context)

@login_required    
def email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            song_list = form.cleaned_data.get('song_list')
            email_list = form.cleaned_data.get('email_list')
            try:
                call_command('SendEmail', 'email_songs', song_list, email_list)
                messages.success(request, 'The selected songs have been emailed.')
            except:
                messages.error(request, 'Email delivery failed.')
            return HttpResponseRedirect('/music/email/')
    else:
        form = EmailForm

    return render(request, 'DrydenMusicApp/email_form.html', {'form':form })
        
def logout(request):
    lgout(request)
    return render(request,'registration/logout.html')
    
def registration(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['email']).exists():
                message = 'There is already a user account with this email.'
                context={'message': message,
                            'form':form}
                return render(request, 'registration/registration.html', context)
            else:
                email_list = ['jessedovi@gmail.com']
                song_list = []
                call_command('SendEmail', 'email_registration', song_list, email_list)
                new_user = form.save()
                return render(request, 'registration/registration_success.html',context={})
    else:
        form = UserCreateForm()
    return render(request, "registration/registration.html", {
        'form': form,
    })
    
@login_required    
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            try:
                form.save()
                messages.success(request, '%s has been added successfully' % title)
            except:
                messages.error(request, 'There was and error uploading.')
            return HttpResponseRedirect('/music/upload/')
        else:
            status = 422 # signal error to UploadProgress
    else:
        form = UploadForm

    return render(request, 'DrydenMusicApp/upload_form.html', {'form':form })
