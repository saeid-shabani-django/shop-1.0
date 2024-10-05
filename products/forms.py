from django.forms import Form
from django import forms
from ckeditor.widgets import CKEditorWidget
from products.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['body','stars']
        widgets:{
            'body':CKEditorWidget(),

        }




