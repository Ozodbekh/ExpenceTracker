from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db.models import CharField


class CustomUserManager(BaseUserManager):
    def _create_user(self, phone_number, fullname, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Telefon raqami kiritilishi shart")

        user = self.model(phone_number=phone_number, fullname=fullname, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, fullname, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, fullname, password, **extra_fields)

    def create_superuser(self, phone_number, fullname="Admin", password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, fullname, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = "phone_number"
    EMAIL_FIELD = "fullname"
    REQUIRED_FIELDS = ["fullname"]
    username = None
    email = None
    objects = CustomUserManager()
    fullname = CharField(max_length=255)
    phone_number = CharField(max_length=15, unique=True)