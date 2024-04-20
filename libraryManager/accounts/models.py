from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from accounts.managers import UserManager
from base.models import TimeStampedModel

# Create your models here.


class GenderType:
    MALE = 1
    FEMALE = 2


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    GENDER_CHOICES = (
        (None, "Please select the gender."),
        (GenderType.MALE, "Male"),
        (GenderType.FEMALE, "Female"),
    )
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=255, blank=True, unique=True, null=True)
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES, null=True, blank=True
    )
    dob = models.DateField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        related_name="custom_user_set",
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        related_name="custom_user_set",
        related_query_name="custom_user",
    )

    USERNAME_FIELD = "email"

    objects = UserManager()
