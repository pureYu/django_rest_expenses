from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile
from expenses.models import Cost


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    costs = serializers.HyperlinkedRelatedField(many=True, view_name='cost-detail', read_only=True)

    class Meta:
        model = Profile
        # fields = ['url', 'id', 'username', 'costs']
        fields = ['url', 'id', 'name', 'surname', 'costs']

