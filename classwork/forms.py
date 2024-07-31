from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    age = forms.IntegerField(required=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'full_name', 'phone_number', 'age', 'gender', 'password1', 'password2')
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        return phone_number

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("You must be 18 years or older to sign up.")
        return age

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput)
    
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(),
        label='Remember Me'
    
    )
    