from rest_framework import serializers

from core.apps.api.models import ListingModel


class BaseListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingModel
        fields = [
            "id",
            "address",
            "full_name",
            "contact_time",
            "category",
            "posting_type",
            "specialty",
            "price",
            "age",
            "bio",
            "phone",
            "telegram",
            "image"
        ]


class ListListingSerializer(BaseListingSerializer):
    class Meta(BaseListingSerializer.Meta): ...


class RetrieveListingSerializer(BaseListingSerializer):
    class Meta(BaseListingSerializer.Meta): ...


class CreateListingSerializer(BaseListingSerializer):
    class Meta(BaseListingSerializer.Meta):
        fields = [
            "id",
            "address",
            "full_name",
            "contact_time",
            "category",
            "posting_type",
            "specialty",
            "price",
            "age",
            "bio",
            "phone",
            "telegram",
            "image",
        ]
