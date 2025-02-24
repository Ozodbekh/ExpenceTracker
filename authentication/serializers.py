import re

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from authentication.models import User


def validate_password(password):
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")

    if not re.search(r'[A-Z]', password):
        raise ValidationError("Password must contain at least one uppercase letter.")

    if not re.search(r'[a-z]', password):
        raise ValidationError("Password must contain at least one lowercase letter.")

    if not re.search(r'\d', password):
        raise ValidationError("Password must contain at least one number.")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError("Password must contain at least one special character.")


class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "phone_number", "fullname", "password"

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("This phone number is already exist!")

        return attrs

    def create(self, validated_data):
        user = User(
            phone_number=validated_data["phone_number"],
            fullname=validated_data["fullname"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user