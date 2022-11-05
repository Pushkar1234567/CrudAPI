from rest_framework.response import Response
from rest_framework import views
from .models import meriDukan
from .serializer import dukanSerializer

class searchDukan(views.APIView):
    def get(self,request):
        obj=meriDukan.objects.all()
        serialize=dukanSerializer(obj,many=True)
        return Response(serialize.data)
