from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Blog
from dobwidget import DateOfBirthWidget


#
# class signup(UserCreationForm):
#     username = forms.CharField(max_length=30, required=True, help_text='')
#     first_name = forms.CharField(max_length=30, required=True, help_text='')
#     last_name = forms.CharField(max_length=30, required=True, help_text='')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
#

class SignUp(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='')
    firstname = forms.CharField(max_length=30, required=True, help_text='')
    lastname = forms.CharField(max_length=30, required=True, help_text='')
    email = forms.EmailField(max_length=254, required=True, help_text='')

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'firstname', 'lastname', 'email')

    def __init__(self, *args, **kwargs):
        super(SignUp, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email')


class diaryEntry(forms.ModelForm):

    subject = forms.CharField(max_length=250)
    entry = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Blog
        fields = ('subject', 'entry')
