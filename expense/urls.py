from django.urls import path

from expense.views import ExpenseCreateAPIView, ExpenseDeleteAPIView, ExpensePutAPIView, ExpenseListAPIView, \
    ExpenseDetailAPIView, ExpenseBalanceAPIView, CategoryListAPIView

urlpatterns = [
    path("expense/create", ExpenseCreateAPIView.as_view()),
    path("expense/delete/<int:pk>", ExpenseDeleteAPIView.as_view()),
    path("expense/update/<int:pk>", ExpensePutAPIView.as_view()),
    path("expense/list", ExpenseListAPIView.as_view()),
    path("expense/detail/<int:pk>", ExpenseDetailAPIView.as_view()),
    path("expense/balance", ExpenseBalanceAPIView.as_view()),
    path("category/<str:type>", CategoryListAPIView.as_view()),
]
