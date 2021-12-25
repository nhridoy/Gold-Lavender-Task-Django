from rest_framework import generics, filters, exceptions
from rest_framework.response import Response

from apiapp import serializers
from mobilephones import models


# Create your views here.

class PhoneApiView(generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    serializer_class = serializers.PhoneSerializer
    queryset = models.Phone.objects.all()
    search_fields = ['model_name', 'jan_code']

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get_queryset(self):
        return models.Phone.objects.all()

    def get(self, request, *args, **kwargs):
        filtered_qs = self.filter_queryset(self.get_queryset())

        serializer = serializers.PhoneSerializer(filtered_qs)
        serializer.is_valid(raise_exception=True)
        if not filtered_qs.exists():
            return Response({'response': 'No Data Found'})
        return Response(serializer.data)
