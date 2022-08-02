from django import forms

from .models import Board


class BoardForm(forms.ModelForm):
    """Form definition for Board."""

    upload_file = forms.FileField(label='첨부 파일', required=False)

    class Meta:
        """Meta definition for Boardform."""

        model = Board  # 이 폼에서 다룰 모델.
        fields = ('title', 'content',)  # 이 폼에서 다룰 필드들.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:300px; resize:none;'}),
            'upload_file': forms.FileInput(attrs={'class': 'form-control'}),
        }  # 특정 필드에 대해 입력 양식을 사용자 임의로 지정.
