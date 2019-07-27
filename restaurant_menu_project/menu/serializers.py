from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class MenuQueryParams(serializers.Serializer):
    search = serializers.CharField(required=False)
    ordering = serializers.ChoiceField(required=False,
                                       choices=['dish', 'price'])
