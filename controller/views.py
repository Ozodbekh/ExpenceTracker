from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from controller.serializers import CategoryCreateSerializer
from expense.models import Category


@extend_schema(tags=["admin"])
class CreateCategoryAPIView(CreateAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CategoryCreateSerializer