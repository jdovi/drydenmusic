from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as lgout
from django.shortcuts import render
from .models import music

# Create your views here.
@login_required
def index(request):

    #select the latest song sheets
    latest_music_list = music.objects.filter(file_type=1)
    latest_music_list = latest_music_list.order_by('-added')[:3]
    
    #select the latest song books
    latest_book_list = music.objects.filter(file_type=2)
    latest_book_list = latest_book_list.order_by('-added')[:3]
    
    #create the context variable
    context = {'latest_music_list': latest_music_list,
            'latest_book_list': latest_book_list,
        }
    return render(request, 'DrydenMusicApp/index.html', context)
    
def sheet_list(request):
    l = music.objects.filter(file_type=1)
    l = l.order_by('title')
    context = {'sheet_list':l}
    return render(request, 'DrydenMusicApp/sheet_list.html', context)
    
def book_list(request):
    l = music.objects.filter(file_type=2)
    l = l.order_by('title')
    context = {'book_list':l}
    return render(request, 'DrydenMusicApp/book_list.html', context)
    
def logout(request):
    lgout(request)
    return render(request,'registration/logout.html')
