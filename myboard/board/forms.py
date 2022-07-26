from django.forms import ModelForm

from .models import Board, Reply


class BoardForm(ModelForm):
    """Form definition for Board."""

    class Meta:
        """Meta definition for Boardform."""

        model = Board
        fields = ('title', 'content',)
