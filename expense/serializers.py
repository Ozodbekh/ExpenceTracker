from rest_framework.serializers import ModelSerializer

from expense.models import Expense, Category


class CreateExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = "id", "amount", "category", "description", "user", "status"
        extra_kwargs = {
            "user": {"write_only": True}
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["category"] = DetailCategorySerializer(
            Category.objects.filter(id=data.get("category")).first()
        ).data
        return data


class DetailCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class DeleteExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = "id", "amount", "description"


class UpdateExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = "id", "amount", "description"


class ListExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = "id", "amount", "description"


class DetailExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = "id", 'amount', 'status', 'category', 'description'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["category"] = DetailCategorySerializer(
            Category.objects.filter(id=data.get("category")).first()
        ).data
        return data


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "id", "name", "status"