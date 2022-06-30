from django import forms
from django.shortcuts import render, redirect

from GamePlay.GamePlay_app.forms import ModelForm, ProfileForm
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
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            form_to_save = form.save(commit=False)
            form_to_save.save()
            return redirect('game_details', form_to_save.id)
    else:
        form = ModelForm()
    context = {
        'form': form,
    }
    return render(request, 'create-game.html', context)


def game_details(request, id):
    model = Model.objects.get(id=id)
    context = {'model': model, }
    return render(request, 'details-game.html', context)


def game_edit(request, id):
    model = Model.objects.get(id=id)
    if request.method == 'POST':
        form = ModelForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ModelForm(instance=model)
    context = {
        'form': form,
        'model': model,
    }
    return render(request, 'edit-game.html', context)


def game_delete(request, id):
    model = Model.objects.get(id=id)
    form = ModelForm(instance=model)
    for field in form.fields:
        form.fields[field].disabled = True
    if request.method == 'POST':
        model.delete()
        return redirect('dashboard')
    context = {
        'model': model,
        'form': form, }
    return render(request, 'delete-game.html', context)


def profile_create(request):
    not_profile = True
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = ProfileForm()
        form.fields['first_name'].widget = forms.HiddenInput()
        form.fields['last_name'].widget = forms.HiddenInput()
        form.fields['profile_picture'].widget = forms.HiddenInput()

    context = {
        'form': form,
        'not_profile': not_profile,
    }
    return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    models = Model.objects.all()
    total_games = len(models)
    if total_games > 0:
        average_rating = sum(model.rating for model in models) / total_games
    else:
        average_rating = 0.0
    full_name = None
    if profile.first_name:
        full_name = profile.first_name
    if profile.last_name:
        if full_name is None:
            full_name = profile.last_name
        else:
            full_name += ' '
            full_name += profile.last_name

    context = {
        'profile': profile,
        'full_name': full_name,
        'total_games': total_games,
        'average_rating': average_rating,
    }
    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = ProfileForm(instance=profile)
    context = {'form': form}
    return render(request, 'edit-profile.html', context)


def delete_models(models):
    if models:
        number = len(models)
        for i in range(len(models)-1, -1, -1):
            model = models[i]
            model.delete()


def profile_delete(request):
    profile = get_profile()
    models = Model.objects.all()
    if request.method == 'POST':
        profile.delete()
        delete_models(models)
        return redirect('home_page')
    return render(request, 'delete-profile.html')
