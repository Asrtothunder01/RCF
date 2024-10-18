from rest_framework_simplejwt.views import  TokenRefreshView
from django.urls import path 
from . import views 


urlpatterns = [
    path('token/', views.CustomTokenObtainPairAPIView.as_view(), name='obtain_token'),
    
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    
    path('signup/', views.SignUpAPIView.as_view(), name='signup'),
    
    path('verify-email/', views.VerifyEmailAPIView.as_view(), name='verify_email'),  
    
    path('resend-otp/', views.ResendOTPAPIView.as_view(), name='resend_otp'),
    
    path('request-password-reset/', views.RequestResetPasswordAPIView.as_view(), name='request_password_reset'),
    
    path('reset-password/', views.ResetPasswordAPIView.as_view(), name='reset_password'),
    
    path('request-change-password/', views.RequestChangePasswordAPIView.as_view(), name='request_change_password'),
    
    path('verify-change-password-otp/', views.VerifyChangePasswordOTPAPIView.as_view(), name='verify_change_password_otp'),
    
    path('change-password/', views.ChangePasswordAPIView.as_view(), name='change_password'),
    
    path('request-change-email/', views.RequestEmailChangeAPIView.as_view(), name='request_change_email'),
    
    path('verify-change-email-otp/', views.VerifyEmailChangeOTPAPIView.as_view(), name='verify_change_email_otp'),
    
    path('change-email/', views.ChangeEmailAPIView.as_view(), name='change_email'),
]