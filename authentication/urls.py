from .views import RegisterView , UsernameValidationView, EmailValidationView, passwordValidationView, VerificationView, LoginView, LogoutView,RequestPasswordResetEmail,CompletePasswordReset
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [ 

    path('register', RegisterView.as_view(),name='register'),
    path('validate-username',csrf_exempt(UsernameValidationView.as_view()),name='validate-username'),
    path('validate-email',csrf_exempt(EmailValidationView.as_view()),name='validate-email'),
    path('validate-password',csrf_exempt(passwordValidationView.as_view()),name='validate-password'),
    path('activate/<uidb64>/<token>',VerificationView.as_view(),name='activate'),
    path('login', LoginView.as_view(),name='login'),
    path('logout', LogoutView.as_view(),name='logout'),
    path('reset-password', RequestPasswordResetEmail.as_view(),name='reset-password'),
    path('password-reset/<uidb64>/<token>',CompletePasswordReset.as_view(),name='reset-user-password'),
    ]