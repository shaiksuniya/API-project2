from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response

class ProductCrud(APIView):
    def get(self,request):
        PQS=product.objects.all()
        PJD=ProductSerializer(PQS,many=True)
        return Response(PJD.data)


    def post(self,request):
       pmsd=ProductSerializer(data=request.data)
       if pmsd.is_valid():
           spo=pmsd.save()
           return Response({'message':'product is created'})
       else:
           return Response({'failed':'product is  not created'})



    def put(self,request):
        id=request.data['id']
        po=product.objects.get(id=id)
        upo=ProductSerializer(po,data=request.data)
        if upo.is_valid():
            upo.save()
            return Response({'message':'product is updated'})
        else:
            return Response({'message':'product is not updated'})


    def patch(self,request,id):
        id=request.data['id']
        po=product.objects.get(id=id)
        po.name=request.data['pname']
        po.save()
        return Response({'success':'Data is partially updated'})  
        



