from rest_framework import serializers
from .models import meriDukan

class dukanSerializer(serializers.Serializer):
    class Meta:
        models : meriDukan
        fields : "__all__"