from typing import Any, Dict
from rest_framework.serializers import ModelSerializer, EmailField, CharField, ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(  # type:ignore
            **validated_data, is_active=False)  
        return user


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)
        user = self.user

        if not user.is_active: #type:ignore
            raise ValidationError('User account is not active.')
        return data
    
class VerifyEmailSerializer(ModelSerializer):
    email = EmailField()
    otp = CharField(max_length=6)

    class Meta:
        model = User
        fields = ['email', 'otp']

class ResendOTPSerializer(ModelSerializer):
    email = EmailField()

    class Meta:
        model = User
        fields = ['email']

class RequestResetPasswordSerializer(ModelSerializer):
    email = EmailField()

    class Meta:
        model = User
        fields = ['email']

class ResetPasswordSerializer(ModelSerializer):
    email = EmailField()
    otp = CharField(max_length=6)
    password = CharField()

    class Meta:
        model = User
        fields = ['email', 'otp', 'password']

    def validate_password(self, value):
        validate_password(value)
        return value
    
class RequestChangePasswordSerializer(ModelSerializer):
    email = EmailField()

    class Meta:
        model = User
        fields = ['email']

class VerifyChangePasswordOTPSerializer(ModelSerializer):
    email = EmailField()
    otp = CharField(max_length=6)

    class Meta:
        model = User
        fields = ['email', 'otp']

class ChangePasswordSerializer(ModelSerializer):
    email = EmailField()
    password = CharField()
    token = CharField(max_length=20)

    class Meta:
        model = User
        fields = ['email', 'password', 'token']

    def validate_password(self, value):
        validate_password(value)
        return value
    
class RequestEmailChangeSerializer(ModelSerializer):
    email = EmailField()

    class Meta:
        model = User
        fields = ['email']

class VerifyEmailChangeOTPSerializer(ModelSerializer):
    email = EmailField()
    otp = CharField(max_length=6)

    class Meta:
        model = User
        fields = ['email', 'otp']


class ChangeEmailSerializer(ModelSerializer):
    email = EmailField()
    new_email = EmailField()
    token = CharField(max_length=20)

    class Meta:
        model = User
        fields = ['email', 'new_email', 'token']


        