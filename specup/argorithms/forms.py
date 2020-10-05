from django import forms
from .models import Argorithm, Comment


class ArgorithmForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
            }
        )
    )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs = {
                'class':'form-control',
            }
        )
    )

    url = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
            }
        )
    )

    class Meta:
        model = Argorithm
        fields = ['title', 'content', 'url']


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
            }
        )
    )

    class Meta:
        model = Comment
        fields = ['content']