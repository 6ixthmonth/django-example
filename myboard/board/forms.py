from django import forms

from .models import Board


class BoardForm(forms.ModelForm):
    """게시글 모델에 대한 폼 클래스."""

    upload_file = forms.FileField(label='첨부 파일', required=False)

    class Meta:
        model = Board
        fields = ('title', 'content',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:300px; resize:none;'}),
            'upload_file': forms.FileInput(attrs={'class': 'form-control'}),
        }
