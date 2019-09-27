from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Cost


class CostFilter(filters.FilterSet):

    class Meta:
        model = Cost
        # fields = ['title', 'author', 'date_spent']
        fields = ['author']

    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    # min_date = filters.DateRangeFilter(field_name="date_spent", lookup_expr='gte')

