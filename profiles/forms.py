from django import forms
from instamain.models import Post
from django.core.exceptions import ValidationError

class FormPost(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].widget.attrs.update({"placeholder": "Add a description"})
        self.fields["title"].widget.attrs.update({"placeholder": "Add a title"})
    class Meta:
        model = Post
        fields = ['images', 'title', 'description']
    
        labels = {
            'images': 'Select a picture',
            'title': 'Title',
            'description': 'Description'
        }

        error_messages = {
            'images': {
                'required': 'You must add a picture'
            },
            'title': {
                'required': 'You need add a title',
                'max_lenght': 'The title must be less than 257 chacarcters'
            }
        }

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40})
        }
    
