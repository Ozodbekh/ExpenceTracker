from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from expense.models import Category


class CategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "name", "status", "icon"

    def validate_name(self, value):
        if Category.objects.filter(name__iexact=value).exists():
            raise ValidationError("A category with this name already exists!")
        return value