from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Cost
from .serializers import CostSerializer

from .filters import *
from django_filters import rest_framework as filters


class CostView(ListCreateAPIView):
    """
    View for listing users' expenses and CRUD their costs
    """
    permission_classes = (IsAuthenticated,)
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CostFilter

    def get_queryset(self):
        # queryset = Cost.objects.filter(author=self.request.user)
        filter = {}
        if IsAuthenticated and self.request.user.id != 1:
            filter['author'] = self.request.user
        queryset = Cost.objects.filter(**filter)
        return queryset.order_by('-date_spent', '-id')

    # def get_queryset(self):
    #     # queryset = Cost.objects.filter(author=self.request.user)
    #     # return queryset.order_by('-date_spent', '-id')
    #
    #     queryset = Cost.objects.all()
    #     filter = {}
    #     filter_text = self.request.query_params.get('search', None)
    #     if filter_text:
    #         filter['title__icontains'] = filter_text
    #     filter_date_form = self.request.query_params.get('date_from', None)
    #     if filter_date_form:
    #         filter['date_spent__gte'] = filter_date_form
    #     return queryset.filter(**filter).order_by('-date_spent', '-id')

    def perform_create(self, serializer):
        author = get_object_or_404(User, id=self.request.user.id)
        return serializer.save(author=author)


class SingleCostView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
