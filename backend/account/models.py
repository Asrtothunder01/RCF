import uuid
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.utils import timezone
from django.utils.crypto import get_random_string

# Create your models here.

def generate_token():
    return get_random_string(64)  # Token generator function

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        Group,
        related_name='account_user_groups',  # Custom related name for groups
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='account_user_permissions',  # Custom related name for permissions
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class OTP(models.Model):
    created_for = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otp')
    otp = models.CharField(max_length=5, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def expired(self):
        expiration_time = self.created_at + timedelta(minutes=5)
        return timezone.now() > expiration_time
    
    def save(self, *args, **kwargs):
        OTP.objects.filter(created_for=self.created_for).delete()  # Clear old OTPs.
        super().save(*args, **kwargs)


class UserActionToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='action_token')
    token = models.CharField(max_length=64, unique=True, default=generate_token)  # Using a named function for the token
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        UserActionToken.objects.filter(user=self.user).delete()  # Clear old tokens.
        super().save(*args, **kwargs)

    def expired(self):
        expiration_time = self.created_at + timedelta(minutes=5)
        return timezone.now() > expiration_time