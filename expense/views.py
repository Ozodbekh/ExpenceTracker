from django.db.models import Sum
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from expense.models import Expense, Category
from expense.serializers import CreateExpenseSerializer, DeleteExpenseSerializer, UpdateExpenseSerializer, \
    ListExpenseSerializer, DetailExpenseSerializer, CategoryListSerializer


@extend_schema(
    tags=["expense"],
    request=CreateExpenseSerializer,
    responses=CreateExpenseSerializer
)
class ExpenseCreateAPIView(CreateAPIView):
    permission_classes = AllowAny,
    queryset = Expense.objects.all()
    serializer_class = CreateExpenseSerializer


class ExpenseDeleteAPIView(APIView):
    permission_classes = IsAuthenticated,

    @extend_schema(
        tags=["expense"],
        request=DeleteExpenseSerializer,
        responses=DeleteExpenseSerializer
    )
    def delete(self, request, pk):
        try:
            expense = Expense.objects.get(pk=pk, user=self.request.user)
        except Expense.DoesNotExist:
            return Response({"detail": "Not found!"}, status=HTTP_404_NOT_FOUND)

        response_data = {
            "id": expense.id,
            "amount": expense.amount,
            "description": expense.description
        }
        expense.delete()
        return Response(response_data, status=HTTP_200_OK)


@extend_schema(tags=["expense"])
class ExpensePutAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateExpenseSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)


@extend_schema(tags=["expense"])
class ExpenseListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)


class ExpenseDetailAPIView(APIView):
    @extend_schema(
        tags=["expense"],
        request=DetailExpenseSerializer,
        responses=DetailExpenseSerializer
    )
    def get(self, request, pk):
        try:
            expense = get_object_or_404(Expense, id=pk, user=self.request.user)
        except Expense.DoesNotExist:
            return Response({"detail": "Not Found!"}, status=HTTP_404_NOT_FOUND)

        srl = DetailExpenseSerializer(expense)
        return Response(srl.data, status=HTTP_200_OK)


@extend_schema(tags=["expense"])
class ExpenseBalanceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_expense = Expense.objects.filter(user=self.request.user)
        income_sum = user_expense.filter(status="income").aggregate(total=Sum("amount"))["total"] or 0
        expense_sum = user_expense.filter(status="expense").aggregate(total=Sum("amount"))["total"] or 0
        total = income_sum - expense_sum

        return Response(
            {
                "total": total,
                "income_sum": income_sum,
                "expense_sum": expense_sum
            }, status=HTTP_200_OK
        )


@extend_schema(tags=["category"])
class CategoryListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, type):
        if type not in ["income", "expense"]:
            return Response({"detail": "Invalid type! Use 'income' or 'expense'."}, status=HTTP_400_BAD_REQUEST)

        categories = Category.objects.filter(status=type)
        serializer = CategoryListSerializer(categories, many=True)

        return Response(serializer.data, status=HTTP_200_OK)
