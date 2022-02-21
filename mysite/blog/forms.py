from django import forms
from blog.models import BlogPost
from mysite.widgets import MyCroppieField


IMG_OPTIONS = {
    'viewport': {
        'width': 180,
        'height': 180,
        'shape': 'square'
        },
    }


class BlogPostForm(forms.ModelForm):
    image = MyCroppieField(label="", options=IMG_OPTIONS, required=False)

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image']
