from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ('name', 'value', 'category',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = '資産名'
        self.fields['value'].widget.attrs['class'] = 'form-control'
        self.fields['value'].widget.attrs['placeholder'] = '金額'
        self.fields['category'].widget.attrs['class'] = 'form-control'


class LiabilityForm(ModelForm):
    class Meta:
        model = Asset
        fields = ('name', 'value', 'category',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = '負債名'
        self.fields['value'].widget.attrs['class'] = 'form-control'
        self.fields['value'].widget.attrs['placeholder'] = '金額'
        self.fields['category'].widget.attrs['class'] = 'form-control'
