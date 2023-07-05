from django.shortcuts import render
#from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import PhoneNumberSerializer ,UserSerializer

class PhoneNumberListAPIView(APIView):
   
    # permission_classes = [IsAuthenticated]
#
    def get(self,request):
        phone_no=Phonenumber.objects.all()
        serializer=PhoneNumberSerializer(phone_no,many=True)
        return Response({
            'status':200,
            'message':'successfull',
            'data':serializer.data
            })
        
           
    def post(self,request):
        try:
            serializer=PhoneNumberSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                
                'status':200,
                'message':'created_success data',
                'data':serializer.data,

                })
            return Response({
                'status':400,
                'message':'Bad request'
            })
            
        except Exception as e:
            print(e)
        return Response({
            'status':False,
            'message':'something went wrong'
        })

#serch by phone_no(get method)
#check no is spam or not(post method)

class SearchByNoAPIView(APIView):
    def get(self,request,phone_no):
        try:
            users = User.objects.filter(phone_no=phone_no)
            serializer = UserSerializer(users,many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
          return Response({"message":"incorrect data"})
        
        
class  MarkNoAsSpamAPIView(APIView):
    def post(self,request):

        return Response({'message': 'Number marked as spam'})
            

        