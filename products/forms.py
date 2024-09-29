from django.forms import Form
from django import forms

from products.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['body','stars']




