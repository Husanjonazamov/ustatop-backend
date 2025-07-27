from django import forms

from core.apps.api.models import PostingModel


class PostingForm(forms.ModelForm):

    class Meta:
        model = PostingModel
        fields = "__all__"
