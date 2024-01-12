from django import forms 
from .models import Post , Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = {'title', 'author'}

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'id': 'elder', 'type': 'hidden'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'content'}

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'title'})
        }
        