from rest_framework import serializers

from core.apps.api.models import PostingTypeModel


class BasePostingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostingTypeModel
        fields = [
            "id",
            "name",
        ]


class ListPostingTypeSerializer(BasePostingTypeSerializer):
    class Meta(BasePostingTypeSerializer.Meta): ...


class RetrievePostingTypeSerializer(BasePostingTypeSerializer):
    class Meta(BasePostingTypeSerializer.Meta): ...


class CreatePostingTypeSerializer(BasePostingTypeSerializer):
    class Meta(BasePostingTypeSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
