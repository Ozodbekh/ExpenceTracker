from django.urls import path

from controller.views import CreateCategoryAPIView

urlpatterns = [
    path("category/create", CreateCategoryAPIView.as_view())
]