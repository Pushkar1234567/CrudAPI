from rest_framework import serializers
from .models import meriDukan

class dukanSerializer(serializers.ModelSerializer):
    class Meta:
        model=meriDukan
        fields = ['id','name','varity','cost','city']
    # class create(self,validated_data):
    #     return meriDukan.objects.create(**validated_data)
