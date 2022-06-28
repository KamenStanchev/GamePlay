from django import forms

from GamePlay.GamePlay_app.models import Profile, Model


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = '__all__'


