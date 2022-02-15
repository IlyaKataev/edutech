from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(label="Почта:", required=True)
    password = forms.CharField(label="Пароль:", widget=forms.PasswordInput(), required=True)
    name = forms.CharField(label="Имя:", required=True)
