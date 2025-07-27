from django_filters import rest_framework as filters

from core.apps.api.models import ListingimageModel, ListingModel


class ListingFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ListingModel
        fields = [
            "name",
        ]


class ListingimageFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ListingimageModel
        fields = [
            "name",
        ]
