from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import CustomUser

# SignUpForm for user registration
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


# SigninForm for user login
class SigninForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        # Authenticate the user using the provided email and password
        if email and password:
            user = authenticate(username=email, password=password)  # Use email as username
            if user is None:
                raise forms.ValidationError("Invalid login credentials.")
            self.user = user  # Store the user object for later use
        return cleaned_data


class CustomUserForm(forms.ModelForm):
    """
    Form for updating user profile (bio and profile picture).
    """
    class Meta:
        model = CustomUser
        fields = ['profile_picture', 'bio', 'username']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically add classes to form fields
        self.fields['username'].widget.attrs.update({'class': 'form-control custom-input'})
        self.fields['bio'].widget.attrs.update({'class': 'form-control custom-input', 'placeholder': 'Tell us about yourself'})
        self.fields['profile_picture'].widget.attrs.update({'class': 'form-control custom-input'})

