from rest_framework import serializers

from core.apps.api.models import PostingModel


class BasePostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostingModel
        fields = [
            "id",
            "name",
        ]


class ListPostingSerializer(BasePostingSerializer):
    class Meta(BasePostingSerializer.Meta): ...


class RetrievePostingSerializer(BasePostingSerializer):
    class Meta(BasePostingSerializer.Meta): ...


class CreatePostingSerializer(BasePostingSerializer):
    class Meta(BasePostingSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
