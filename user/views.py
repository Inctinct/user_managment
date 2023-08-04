from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import RegistrationSerializer, UserProfileSerializer

from .models import RegisteredUser


class RegistrationView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = RegisteredUser.objects.get(email=self.request.user)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        data["email"] = self.request.user.email
        serializer = UserProfileSerializer(data=data)
        serializer.is_valid()
        RegisteredUser.objects.filter(email=self.request.user).update(**request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        RegisteredUser.objects.filter(email=self.request.user).delete()
        return Response(status=status.HTTP_200_OK)
