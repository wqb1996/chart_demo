from rest_framework import serializers
from .models import ChartInfo


class ChartInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartInfo
        fields = "__all__"
        read_only_fields = ['id']
        extra_kwargs = {
            'CDN': {'required': False, 'default': ''},
        }
