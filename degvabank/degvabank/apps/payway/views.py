from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

from .serializers import PayWayKeysSerializer, UserPayWayKeysSerializer, PayWayMetaSerializer, UserPayWayMetaSerializer
from .models import PayWayKeys, PayWayMetaData
from ..user.models import User

class PaywayKeysViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for payway keys
    """

    permission_classes = (IsAdminUser,)
    queryset = PayWayKeys.objects.all()
    serializer_class = PayWayKeysSerializer

class UserPaywayKeysCreateView(generics.CreateAPIView):

    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = UserPayWayKeysSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        try:
            # may not exist
            request.user.key_pair.delete()
        except User.key_pair.RelatedObjectDoesNotExist:
            pass
        return super().create(request, *args, **kwargs)


class PaywayMetaViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for payway keys
    """

    permission_classes = (IsAdminUser,)
    queryset = PayWayMetaData.objects.all()
    serializer_class = PayWayMetaSerializer



class UserPaywayKeysCreateView(generics.ListCreateAPIView):

    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = UserPayWayKeysSerializer
    permission_classes = (IsAuthenticated,)
