from django.urls import re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView

from user.views import RegistrationView, UserProfileView

urlpatterns = [
    re_path("register/", RegistrationView.as_view()),
    re_path("profile/", UserProfileView.as_view()),
    re_path(r"^login/", TokenObtainPairView.as_view(), name="login"),
    re_path(r"^token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    re_path(r"^token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    re_path(r"^logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
]
