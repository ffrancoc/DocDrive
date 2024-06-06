from django.contrib.auth import logout, get_user
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import forms
from .models import Archive, User
from .utils import Utils
from django.contrib import messages
import os


def index(request):
    return redirect('login')

@login_required
def logout_session(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('login')        

    form = forms.CustomUserCreationForm()
    return render(request, 'registration/register.html', context={'form': form})


@login_required
def remove_file(request):
    user = get_user(request)
    if request.method == 'POST':        
        file_id = request.POST['file_id']

        obj = Archive.objects.filter(id=file_id, user_id=user.id)
        obj[0].file.delete()
        obj.delete()
        messages.add_message(request, messages.SUCCESS, 'Archivo Eliminado')        
        
    return redirect('my_media')


@login_required
def my_media(request):
    user = get_user(request)
    
    if request.method == 'POST':
        form = forms.ArchiveForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']

            file_extension = Utils.file_extension(file.name)            
            file_bytes = len(file.file.read())


            obj = form.save(commit=False)
            obj.user = get_user(request)            
            obj.file_type = file_extension
            obj.file_size = Utils.file_size(file_bytes)
            obj.save()

            messages.add_message(request, messages.SUCCESS, f'El Archivo {obj.title} fue subido exitosamente')

            return redirect('my_media')

    
    (media_directory, media_size) =Utils.user_media_directory(request, user)
    


    total_images = 0
    total_files = 0
    data = []
    if os.path.exists(media_directory):
        user_media = os.listdir(media_directory)

        archives = Archive.objects.all().filter(user=user)[::1]

        total_images = Archive.objects.filter(file_type__in=['.jpg', '.png'], user_id=user.id).count()        
        total_files = Archive.objects.filter(file_type__in=['.pdf'], user_id=user.id).count()                
        data = []

        for archive in archives:
            for media in user_media:
                if os.path.basename(archive.file.path) == media:
                    data.append(archive)        

    form = forms.ArchiveForm()


    users = User.objects.all().filter(is_active=1)[::1]

    context = {
        'total_images': total_images,
        'total_files': total_files,
        'media_size': media_size,
        'users': users,
        'data': data,
        'form': form
    }

    return render(request, 'my-drive.html', context=context)
    
            