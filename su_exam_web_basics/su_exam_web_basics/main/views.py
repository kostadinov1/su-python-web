from django.shortcuts import render, redirect

from su_exam_web_basics.main.forms import CreateProfileForm, DeleteProfileForm, CreateAlbumForm, EditAlbumForm, \
    DeleteAlbumForm
from su_exam_web_basics.main.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def show_home(request):
    profile = get_profile()

    if not profile:
        return redirect('show home no profile')

    albums = profile.album_set.all()
    context = {
        'albums': albums,
        'profile': profile,
    }

    return render(request, 'home-with-profile.html', context)


def show_add_album(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST, instance=Album(username_id=profile))
        if form.is_valid():
            form.save()
            return redirect('show home with profile')
    else:
        form = CreateAlbumForm(instance=Album(username_id=profile))

    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def show_edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show home with profile')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'edit-album.html', context)


def show_delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show home with profile')

    form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
        'pk': pk,
    }
    return render(request, 'delete-album.html', context)


def show_album_details(request, pk):
    profile = get_profile()
    album = profile.album_set.get(pk=pk)

    context = {
        'profile': profile,
        'album': album,
        'pk': pk,
    }

    return render(request, 'album-details.html', context)


def show_create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home with profile')

    form = CreateProfileForm()

    context = {
        'form': form
    }

    return render(request, 'home-no-profile.html', context)


def show_profile_details(request):
    profile = get_profile()
    albums_count = profile.album_set.all()

    context = {
        'profile': profile,
        'albums_count': len(albums_count)
    }

    return render(request, 'profile-details.html', context)


def show_profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show home no profile')

    form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'profile-delete.html', context)
