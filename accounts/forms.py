from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms



class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    labels = {
        'username': 'UserId',
        'password1': 'Password',
        'password2': 'Confirm Password'
    }
    def __init__(self, *args, **kwargs):
        super(UserRegister, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = True
            self.fields[field_name].widget.attrs['class'] = 'form-control'

class UserLogin(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    labels = {
        'username': 'UserId',
        'password': 'Password'
    }
    def __init__(self, *args, **kwargs):
        super(UserLogin, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = True
            self.fields[field_name].widget.attrs['class'] = 'form-control'


