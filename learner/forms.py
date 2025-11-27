from django import forms
from learner.models import Post

class PostForm(forms.ModelForm):
    class Meta:
       model = Post
       fields = ['title', 'description', 'status']
        