import forms
from instamain.models import Post


class form_post(forms.ModelForm):
    model = Post
    
