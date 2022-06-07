from django import forms
from .models import Profile, Post, Comment
from django.contrib.auth.models import User

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
    # comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Write comment'}), required=True)
    class Meta:
        model = Comment
        exclude = ['post', 'user', 'date']