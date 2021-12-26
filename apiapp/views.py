from django.db.models import Q
from rest_framework import generics, filters, exceptions
from rest_framework.response import Response

from apiapp import serializers
from mobilephones import models
from django.core import serializers as ds
from django.http import HttpResponse
from django.forms.models import model_to_dict


# Create your views here.

class PhoneApiView(generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    serializer_class = serializers.PhoneSerializer
    queryset = models.Phone.objects.all()
    search_fields = ['model_name', 'jan_code']

    # def get_queryset(self):
    #     search = self.request.query_params.get('search')
    #     filter_qs = models.Phone.objects.filter(Q(model_name__icontains=search) | Q(jan_code__contains=search))
    #     return filter_qs
    #
    # def list(self, request, *args, **kwargs):
    #     ser = self.get_serializer(self.get_queryset(), many=True)
    #     responseData = ser.data
    #     search = self.request.query_params.get('search')
    #     filter_qs = models.Phone.objects.filter(Q(model_name__icontains=search) | Q(jan_code__contains=search))
    #     if not filter_qs.exists():
    #         return Response({'response': 'No Data Found'})
    #     return Response(responseData)

    # def filter_queryset(self, queryset):
    #     for backend in list(self.filter_backends):
    #         queryset = backend().filter_queryset(self.request, queryset, self)
    #     return queryset





    # def get_queryset(self):
    #     return models.Phone.objects.all()
    #
    # def get(self, request, *args, **kwargs):
    #     filtered_qs = self.filter_queryset(self.get_queryset())
    #
    #     serializer = serializers.PhoneSerializer(filtered_qs, data=request.data)
    #     print(request.data)
    #     serializer.is_valid(raise_exception=True)
    #     if not filtered_qs.exists():
    #         return Response({'response': 'No Data Found'})
    #     return Response(serializer.data)
