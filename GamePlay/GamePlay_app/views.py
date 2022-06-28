from django.shortcuts import render

from GamePlay.GamePlay_app.models import Profile, Model


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]


def home_page(request):
    profile = get_profile()
    if profile:
        model = Model.objects.all()
        context = {
            'model': model,
        }
        return render(request, 'home-page.html', context)
    else:
        not_profile = True
        context = {
            'not_profile': not_profile,
        }
        return render(request, 'home-page.html', context)

def dashboard(request):
    profile = get_profile()
    if profile:
        model = Model.objects.all()
        context = {
            'model': model,
        }
        return render(request, 'dashboard.html', context)
    else:
        not_profile = True
        context = {
            'not_profile': not_profile,
        }

    return render(request, 'dashboard.html', context)


def game_create(request):
    return render(request, 'create-game.html')


def game_details(request):
    return render(request, 'details-game.html')

def game_edit(request):
    return render(request, 'edit-game.html')

def game_delete(request):
    return render(request, 'delete-game.html')

def profile_create(request):
    return render(request, 'create-profile.html')

def profile_details(request):
    return render(request, 'details-profile.html')

def profile_edit(request):
    return render(request, 'edit-profile.html')

def profile_delete(request):
    return render(request, 'delete-profile.html')
