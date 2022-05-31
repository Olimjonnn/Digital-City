from rest_framework import serializers
from main.models import *


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"

class AboutTexnoParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutTexnoPark
        fields = "__all__"

class InformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informations
        fields = "__all__"

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"

class ContactUSSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUS
        fields = "__all__"

class GrafikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grafik
        fields = "__all__"

class MaqsadliAuditoriyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaqsadliAuditoriya
        fields = "__all__"

class ProtsentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protsent
        fields = "__all__"

class DCSerializer(serializers.ModelSerializer):
    class Meta:
        model = DC
        fields = "__all__"

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = "__all__"

class XizmatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xizmat
        fields = "__all__"

class XizmatSendSerializer(serializers.ModelSerializer):
    class Meta:
        model = XizmatSend
        fields = "__all__"
