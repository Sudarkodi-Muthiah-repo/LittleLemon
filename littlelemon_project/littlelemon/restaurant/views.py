from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from .models import Booking,MenuItem,Menu
from .serializers import BookingSerializer,menuSerializer,MenuItemSerializer,UserSerializer
from rest_framework import viewsets,permissions
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request,'index.html',{})


# class Bookingview(APIView):

#     def get(self,request):
#         items = Booking.objects.all()
#         serializer = BookingSerializer(items,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = menuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status":"success","data":serializer.data})
    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] 


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


