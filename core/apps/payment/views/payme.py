from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.payment.models import PaymeModel
from core.apps.payment.serializers.payme import CreatePaymeSerializer, ListPaymeSerializer, RetrievePaymeSerializer


@extend_schema(tags=["payme"])
class PaymeView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = PaymeModel.objects.all()
    serializer_class = ListPaymeSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListPaymeSerializer,
        "retrieve": RetrievePaymeSerializer,
        "create": CreatePaymeSerializer,
    }
