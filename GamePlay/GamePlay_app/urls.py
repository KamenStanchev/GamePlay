from django.urls import path
from GamePlay.GamePlay_app.views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('dashboard/', dashboard, name='dashboard'),

    path('game/create/', game_create, name='game_create'),
    path('game/details/<id>/', game_details, name='game_details'),
    path('game/edit/<id>/', game_edit, name='game_edit'),
    path('game/delete/<id>/', game_delete, name='game_delete'),

    path('profile/create', profile_create, name='profile_create'),
    path('profile/details/', profile_details, name='profile_details'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('profile/delete/', profile_delete, name='profile_delete'),

]
