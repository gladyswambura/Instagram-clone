from django import forms
from .models import Profile, Post, Comment
from django.contrib.auth.models import User

# AUTHENTICATION
# class UserRegisterForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'prompt srch_explore'}), max_length=50, required=True)
#     email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'prompt srch_explore'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'prompt srch_explore'}))

#     class Meta:
#         model = User
#         widgets = {
#             'username' : forms.TextInput(attrs = {'placeholder': 'Username'}),
#             'email'    : forms.TextInput(attrs = {'placeholder': 'E-Mail'}),
#             'password'    : forms.TextInput(attrs = {'placeholder': 'password'}),
#         }
#         fields = ['username', 'email', 'password1', 'password2']

# PROFILE
class UpdateProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['image','bio']

class NewProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['image','bio']

# UPDATE USER
class UpdateUserForm(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']

# POST
class NewPostform(forms.ModelForm):
    picture = forms.ImageField(required=True)
    caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Caption'}), required=True)

    class Meta:
        model = Post
        fields = ['picture', 'caption']

# COMMENT
class NewCommentForm(forms.ModelForm):
    # body = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Write comment'}), required=True)
    class Meta:
        model = Comment
        exclude = ['post', 'user', 'date']