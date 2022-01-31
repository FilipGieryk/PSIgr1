from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User



class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'password1', 'password2']