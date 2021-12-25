from rest_framework import serializers

from mobilephones import models


class PhoneSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand')

    class Meta:
        model = models.Phone
        fields = '__all__'
