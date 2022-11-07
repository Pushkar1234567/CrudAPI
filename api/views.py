from rest_framework.response import Response
from rest_framework import views
from .models import meriDukan
from .serializer import dukanSerializer

class searchDukan(views.APIView):
    def get(self,request,pk=None):
        if pk is not None:
            obj=meriDukan.objects.filter(pk=pk).first()
            serialize=dukanSerializer(obj)
            return Response(serialize.data)
        obj=meriDukan.objects.all()
        serialize=dukanSerializer(obj,many=True)
        return Response(serialize.data)
    def post(self,request):
        data=request.data
        serializer=dukanSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data successfully Created'})
        return Response (serializer.errors)
    def put(self,request,pk):
        if pk is not None:
            obj=meriDukan.objects.filter(pk=pk).first()
            serilarzer=dukanSerializer(obj,data=request.data)
            serilarzer.is_valid(raise_exception=True)
            serilarzer.save()
            return Response("data successfully Updated")
        return Response("Your entered id is not here")
    def delete(self,request,pk):
        obj=meriDukan.objects.filter(pk=pk).first()
        obj.delete()
        return Response("User deleted")

