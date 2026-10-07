from rest_framework import serializers
from .models import *



class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ["name", "email", "tracking_id"]  
        

class TrackingPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingPackage
        fields = '__all__'
        

class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'

        

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"



class PhonealertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonealert
        fields = "__all__"
       
