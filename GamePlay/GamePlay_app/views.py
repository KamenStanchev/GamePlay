from django.shortcuts import render


def home_page(request):
    return render(request, 'home-page.html')


def dashboard(request):
    return render(request, 'dashboard.html')

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
