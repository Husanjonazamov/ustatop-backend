from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import PostingModel
from core.apps.api.serializers.posting import CreatePostingSerializer, ListPostingSerializer, RetrievePostingSerializer


@extend_schema(tags=["posting"])
class PostingView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = PostingModel.objects.all()
    serializer_class = ListPostingSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListPostingSerializer,
        "retrieve": RetrievePostingSerializer,
        "create": CreatePostingSerializer,
    }
