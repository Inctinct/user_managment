from django.urls import re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

from user.views import RegistrationView, UserProfileView

"""
 register/ - post(user registration),
 profile/ - get(give information about user), put(change user profile information), delete(delete user account)
 login/ - post(login user with email and password) response - access and refresh tokens
 token/refresh - post(refresh user token)
 token/verify - post(verify user token)
 logout - post(logout user)
"""
urlpatterns = [
    re_path("register/", RegistrationView.as_view()),
    re_path("profile/", UserProfileView.as_view()),
    re_path(r"^login/", TokenObtainPairView.as_view(), name="login"),
    re_path(r"^token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    re_path(r"^token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    re_path(r"^logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
]
