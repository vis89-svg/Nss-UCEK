from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'style': 'box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25)'
            }),
        
        label=''
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'style': 'box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25)'
            }),
        label=''
    )
