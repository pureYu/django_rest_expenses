from rest_framework import serializers

from .models import Cost

# class CostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     amount = serializers.DecimalField(max_digits=6, decimal_places=2)
#     date_spent = serializers.DateTimeField()
#     author_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Cost.objects.create(**validated_data)
#     # author = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.amount = validated_data.get('amount', instance.amount)
#         instance.date_spent = validated_data.get('date_spent', instance.body)
#         instance.author_id = validated_data.get('author_id', instance.author_id)
#         instance.save()
#         return instance

# class CostSerializer(serializers.ModelSerializer):
class CostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Cost
        fields = ('id', 'title', 'amount', 'date_spent', 'author_id', 'author')
