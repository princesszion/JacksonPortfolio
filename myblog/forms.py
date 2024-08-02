from django import forms
from .models import BlogPost
from .models import Contact

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author', 'image']



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'organisation', 'email', 'phone', 'subject', 'message']
