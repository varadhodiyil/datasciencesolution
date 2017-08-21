from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    company = serializers.CharField(max_length=250)
    phone = serializers.CharField(max_length=12,min_length=10)
    requirement = serializers.CharField(max_length=1000)
    class Meta:
        fields ='__all__'


