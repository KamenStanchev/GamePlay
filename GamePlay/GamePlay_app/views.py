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
    models = Model.objects.all()
    if not models:
        models = None

    context = {
        'models': models,
    }

    return render(request, 'dashboard.html', context)


def game_create(request):
    return render(request, 'create-game.html')


def game_details(request, id):
    model = Model.objects.get(id=id)
    context = {'model': model, }
    return render(request, 'details-game.html', context)


def game_edit(request):
    return render(request, 'edit-game.html')


def game_delete(request):
    return render(request, 'delete-game.html')


def profile_create(request):
    return render(request, 'create-profile.html')


def profile_details(request):
    profile = get_profile()
    models = Model.objects.all()
    total_games = len(models)
    if total_games > 0:
        average_rating = sum(model.rating for model in models)/total_games
    else:
        average_rating = 0.0
    full_name = profile.first_name + ' ' + profile.last_name

    context = {
        'profile': profile,
        'full_name': full_name,
        'total_games': total_games,
        'average_rating': average_rating,
    }
    return render(request, 'details-profile.html', context)


def profile_edit(request):
    return render(request, 'edit-profile.html')


def profile_delete(request):
    return render(request, 'delete-profile.html')
