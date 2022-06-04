from django import forms

from .models import Theme, Comment


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = (
            'text',
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {
            'text',
        }
