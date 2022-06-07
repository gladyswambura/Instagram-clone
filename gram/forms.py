from django import forms
from .models import Profile, Post, Comment
from django.contrib.auth.models import User
from django.forms import ModelForm

# PROFILE
class UpdateProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['image','bio']

class NewProfileForm(forms.ModelForm):
    class Meta:
      model = Profile
      exclude = ['user']  # exclude the user field

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
  class Meta:
    model = Comment
    fields = "__all__"