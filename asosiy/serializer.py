from rest_framework import serializers
from .models import *

class KursSerialzer(serializers.Serializer):
    class Meta:
        model = Kurs
        fields = '__all__'

class UstozSerialzer(serializers.Serializer):
    class Meta:
        model = Ustoz
        fields = '__all__'

class XonaSerializer(serializers.Serializer):
    class Meta:
        model = Xona
        fields = '__all__'

class OquvchiSerializer(serializers.Serializer):
    class Meta:
        model = Oquvchi
        fileds = '__all__'

class GuruhSerializer(serializers.Serializer):
    class Meta:
        model = Guruh
        fields = '__all__'

class TolovSerializer(serializers.Serializer):
    class Meta:
        model = Tolov
        fields = '__all__'

class DavomatSerializer(serializers.Serializer):
    class Meta:
        model = Davomat
        fields = '__all__'