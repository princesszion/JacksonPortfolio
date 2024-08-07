from django import forms
from .models import BlogPost
from .models import Contact

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author', 'image']



# # forms.py
# from django import forms
# from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'organisation', 'email', 'phone', 'subject', 'message']
        labels = {
            'full_name': 'Full Name',
            'organisation': 'Organisation',
            'email': 'Email',
            'phone': 'Phone',
            'subject': 'Subject',
            'message': 'Message',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your Full Name'}),
            'organisation': forms.TextInput(attrs={'placeholder': 'Your Organisation'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Phone Number'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message'}),
        }
