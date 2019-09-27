from rest_framework import serializers

from .models import Cost


class CostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    date_spent = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    # date_spent = serializers.DateTimeField(format='%Y-%m-%d')
    # time_spent = serializers.DateTimeField(format='%H:%M', source='date_spent')

    class Meta:
        model = Cost
        fields = ('id', 'title', 'amount', 'date_spent', 'author_id', 'author')
