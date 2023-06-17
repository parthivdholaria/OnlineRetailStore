from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

# registration form


class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # ensures that this field is mandatory
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True

    def clean_email(self):

        email = self.cleaned_data.get("email")

        if (User.objects.filter(email=email).exists()):
            raise forms.ValidationError("Invalid email! Email already used")

        if (len(email) >= 250):
            raise forms.ValidationError("Email is too long")

        return email


# login form

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:

        model = User

        fields = ['username', 'email']
        exclude = ['password1', 'password1']

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True

    # Email validation

    def clean_email(self):

        email = self.cleaned_data.get("email")

        # allows the user to only update the username and leave the original email unchanged
        #else if he changes to any other email that already exists in database then it raises error
        # however it does not raise any error if the current email he entered is the user's own email address
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():

            raise forms.ValidationError('This email is invalid')

        # len function updated ###

        if len(email) >= 350:

            raise forms.ValidationError("Your email is too long")

        return email
