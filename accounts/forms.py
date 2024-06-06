from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm#djangoのデフォルトの認証関連のフォーム
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 
                'last_name', 'is_active')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 
                'age', 'is_active')


class LoginAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                (" アカウントが無効です "),
                code='inactive',
            )
        if not user.is_admin:
            raise forms.ValidationError(
            (" 管理者権限を持っていません "),
            code='notadmin'
            )