from django import forms

from .models import Board


class BoardForm(forms.ModelForm):
    """Form definition for Board."""

    class Meta:
        """Meta definition for Boardform."""

        model = Board
        fields = ('title', 'content',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:300px; resize:none;'}),
        }
