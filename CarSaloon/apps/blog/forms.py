from django import forms
from .models import *


#To make form for our blog
class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','description','is_active','main_img']