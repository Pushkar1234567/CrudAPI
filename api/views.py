from rest_framework.response import Response
from rest_framework import views
from .models import meriDukan
from .serializer import dukanSerializer

class searchDukan(views.APIView):
    def get(self,request):
        obj=meriDukan.objects.all()
        serialize=dukanSerializer(obj,many=True)
        return Response(serialize.data)

    def retrieve(self,request,pk):
        obj=meriDukan.object.filter(id=pk).first()
        if not obj:
            return Response("Not data present")
        serializer=dukanSerializer(obj)
        return Response(serializer.data)

    def post(self,request):
            serializer=dukanSerializer(data=request.data, is_tombstoned=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'msg':'Data successfully Created'})
            return Response (serializer.errors)
    def update(self,request,pk):
        if pk is not None:
            obj=meriDukan.objects.filter(pk=pk).first()
            serilarzer=dukanSerializer(obj,data=request.data)
            serilarzer.is_valid(raise_exception=True)
            serilarzer.save()
            return Response("data successfully Updated")
        return Response("Your entered id is not here")
    def destroy(self,request,pk):
        obj=meriDukan.objects.filter(id=pk,is_tombstoned=True).first()
        obj.delete()
        return Response("User deleted")

