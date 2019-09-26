from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Cost
from .serializers import CostSerializer


class CostViewSet(viewsets.ModelViewSet):
    serializer_class = CostSerializer
    queryset = Cost.objects.all()


# from rest_framework.generics import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from .models import Cost
# from .serializers import CostSerializer
#
#
# class CostView(APIView):
#     def get(self, request):
#         costs = Cost.objects.all()
#         serializer = CostSerializer(costs, many=True)
#         return Response({"costs": serializer.data})
#
#     def post(self, request):
#         cost = request.data.get('cost')
#         # Create the cost from the above data
#         serializer = CostSerializer(data=cost)
#         if serializer.is_valid(raise_exception=True):
#             cost_saved = serializer.save()
#         return Response({"success": "Cost '{} / {}' created successfully".format(cost_saved.amount, cost_saved.title)})
#
#     def put(self, request, pk):
#         saved_cost = get_object_or_404(Cost.objects.all(), pk=pk)
#         data = request.data.get('cost')
#         serializer = CostSerializer(instance=saved_cost, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             cost_saved = serializer.save()
#         return Response({
#             "success": "Cost '{} / {}' updated successfully".format(cost_saved.amount, cost_saved.title)
#         })
#
#     def delete(self, request, pk):
#         # Get object with this pk
#         cost = get_object_or_404(Cost.objects.all(), pk=pk)
#         cost.delete()
#         return Response({
#             "message": "Cost with id `{}` has been deleted.".format(pk)
#         }, status=204)


# from django.shortcuts import get_object_or_404
# from rest_framework import viewsets
# from rest_framework.response import Response
#
# from .models import Cost
# from .serializers import CostSerializer
#
#
# class CostView(viewsets.ViewSet):
#     """
#     A simple ViewSet that for listing or retrieving users.
#     """
#
#     def list(self, request):
#         queryset = Cost.objects.all()
#         serializer = CostSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Cost.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = CostSerializer(user)
#         return Response(serializer.data)