from django.contrib import admin

# Register your models here.
from GamePlay.GamePlay_app.models import Profile, Model

admin.site.register(Profile)
admin.site.register(Model)
