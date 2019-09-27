from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # username = serializers.ReadOnlyField(source='user.username')
    # email = serializers.ReadOnlyField(source='user.email')
    # user_id = serializers.ReadOnlyField(source='user.username')

    # class Meta:
    #     model = Profile
    #     fields = ('id', 'name', 'surname', 'user', 'username', 'email')
    #     read_only_fields = ('user',)

    class Meta:
        model = Profile
        fields = ('id', 'name', 'surname','user')
        read_only_fields = ('user',)

        # def update(self, instance, validated_data):
        #     user = validated_data.get('user')
        #     # instance.user.first_name = user.get('first_name')
        #     instance.user.save()
        #     print("hey")
        #     return instance

    # def create(self, validated_data):
    #     # create user
    #     user = User.objects.create(
    #         # url = validated_data['url'],
    #         email = validated_data['email'],
    #     )
    #     profile_data = validated_data.pop('profile')
    #     # create profile
    #     profile = Profile.objects.create(
    #         user = user,
    #         name = profile_data['name'],
    #         surname = profile_data['surname'],
    #     )
    #
    #     return user
