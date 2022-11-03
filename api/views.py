from django.shortcuts import render
from httplib2 import Response
from requests import request
from rest_framework import views
from yaml import serialize
from .models import meriDukan
from .serializer import dukanSerializer

class searchDukan(views.APIView):
    def get(self,request):
        obj=meriDukan.objects.all()
        serialize=dukanSerializer(obj,many=True, safe=False)
        return Response(serialize.data)
