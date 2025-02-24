from django.db.models import Model, TextChoices, ImageField, ForeignKey, CASCADE
from django.db.models.fields import CharField, BigIntegerField, TextField


class Type(TextChoices):
    income = "income", "Income"
    expense = "expense", "Expense"


class Category(Model):
    name = CharField(max_length=255)
    status = CharField(max_length=15, choices=Type, default=Type.income)
    icon = ImageField(upload_to="media/icons", null=True, blank=True)


class Expense(Model):
    amount = BigIntegerField(default=0)
    status = CharField(max_length=15, choices=Type, default=Type.income)
    description = TextField(null=True, blank=True)
    category = ForeignKey("expense.Category", on_delete=CASCADE, related_name="expenses")
    user = ForeignKey("authentication.User", on_delete=CASCADE, related_name="expenses")