from django.db.models import Q
from rest_framework import generics, filters, status
from rest_framework.response import Response

from apiapp import serializers
from mobilephones import models


# Create your views here.

class PhoneApiView(generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    serializer_class = serializers.PhoneSerializer
    search_fields = ['model_name', 'jan_code']

    def get_queryset(self):
        try:
            search = self.request.query_params.get('search')
            return models.Phone.objects.filter(
                Q(model_name__icontains=search) | Q(jan_code__contains=search)
            )

        except:
            return models.Phone.objects.all()

    def get(self, request, *args, **kwargs):
        data = self.get_serializer(self.get_queryset(), many=True).data
        if len(data) > 0:
            return Response(data, status=status.HTTP_200_OK)
        context = {
            "message": "No Data Found"
        }
        return Response(context, status=status.HTTP_200_OK)
