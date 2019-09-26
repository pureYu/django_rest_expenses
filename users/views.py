from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from  expenses.models import Cost
from .serializers import ProfileSerializer


class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class ProfileFilterView(APIView):
    pass
    # def get(self, request, region):
    #     users = Profile.objects.filter(city=region) | Profile.objects.filter(country=region)
    #     return Response({"users": users}, status=status.HTTP_200_OK)


class ProfileExistsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
            return Response({"result": True, "id": profile.id})
        except Profile.DoesNotExist:
            return Response({"result": False})


class ProfileEditDeleteRetrieveView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)


# from django.shortcuts import render
# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from rest_auth.registration.views import SocialLoginView
#
#
# class FacebookLogin(SocialLoginView):
#     adapter_class = FacebookOAuth2Adapter
#

