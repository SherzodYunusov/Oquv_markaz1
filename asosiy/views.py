from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *


class KursApiView(APIView):
    def get(self, request):
        kurs = Kurs.objects.all()
        serializer = KursSerialzer(kurs, many=True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        serializer = KursSerialzer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class UstozApiView(APIView):
    def get(self, request):
        ustoz = Ustoz.objects.all()
        serializer = UstozSerialzer(ustoz, many=True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        serializer = UstozSerialzer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class XonaApiView(APIView):
    def get(self, requset):
        xona = Xona.objects.all()
        serializer = XonaSerializer(xona, many=True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        serializer = XonaSerializer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OquvchiApiView(APIView):
    def get(self, requset):
        oquvchi = Oquvchi.objects.all()
        serializer = OquvchiSerializer(oquvchi, many=True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        serializer = OquvchiSerializer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GuruhApiView(APIView):
    def get(self, requset):
        guruh = Guruh.onjects.all()
        serializer = GuruhSerializer(guruh, many=True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        serializer = GuruhSerializer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TolovApiView(APIView):
    def get(self, requset):
        tolov = Tolov.onjects.all()
        serializer = TolovSerializer(tolov, many=True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        serializer = TolovSerializer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DavomatApiView(APIView):
    def get(self, requset):
        davomat = Davomat.onjects.all()
        serializer = DavomatSerializer(davomat, many=True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        serializer = DavomatSerializer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
