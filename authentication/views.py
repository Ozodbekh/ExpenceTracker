from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from authentication.models import User
from authentication.serializers import RegisterUserSerializer


@extend_schema(
    tags=["api"],
    request=RegisterUserSerializer,
    responses=RegisterUserSerializer
)
class UserRegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer
