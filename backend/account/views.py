from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.utils import timezone
from .models import User, OTP, UserActionToken
from django.utils.crypto import get_random_string
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail

# User Registration API View
class RegisterUserAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email is already registered'}, status=status.HTTP_400_BAD_REQUEST)

        # Create user
        user = User.objects.create_user(email=email, password=password, is_active=False)
        
        # Generate OTP for user
        otp_code = get_random_string(5, '0123456789')
        OTP.objects.create(created_for=user, otp=otp_code)

        # Send OTP via email (dummy function, you should implement it)
        send_mail(
            'Your OTP Code',
            f'Your OTP code is {otp_code}',
            'admin@churchapp.com',
            [user.email],
            fail_silently=False,
        )

        return Response({'message': 'User registered. OTP sent to email.'}, status=status.HTTP_201_CREATED)


# User Login API View
class LoginUserAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Account is not activated. Please verify OTP.'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)


# OTP Verification API View
class VerifyOTPAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        otp_code = request.data.get('otp')

        try:
            user = User.objects.get(email=email)
            otp = OTP.objects.filter(created_for=user, otp=otp_code).first()

            if otp and not otp.expired():
                user.is_active = True
                user.save()
                otp.delete()  # Delete OTP after successful verification
                return Response({'message': 'OTP verified, account activated.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid or expired OTP'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


# User Action Token API View (e.g., password reset)
class UserActionTokenAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, token):
        try:
            action_token = UserActionToken.objects.get(token=token, is_used=False)
            
            if action_token.expired():
                return Response({'error': 'Token expired'}, status=status.HTTP_400_BAD_REQUEST)

            # Mark the token as used after action (e.g., password reset)
            action_token.is_used = True
            action_token.save()

            return Response({'message': 'Action completed successfully.'}, status=status.HTTP_200_OK)
        except UserActionToken.DoesNotExist:
            return Response({'error': 'Invalid or used token'}, status=status.HTTP_404_NOT_FOUND)