from this import d
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, action, APIView
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, CreateAPIView
from .models import * 
from .serializer import *


class SliderView(RetrieveAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

    def retrieve(self, request, pk):
        slider = Slider.objects.get(id=pk)
        sld = SliderSerializer(slider)
        return Response(sld.data)

    

class AboutTexnoParkView(ListAPIView):
    queryset = AboutTexnoPark.objects.all()
    serializer_class = AboutTexnoParkSerializer

    def list(self, request):
        texna = AboutTexnoPark.objects.all().order_by("id")[0:6]
        texn = AboutTexnoParkSerializer(texna, many=True)
        return Response(texn.data)

    
class InformationsView(RetrieveAPIView):
    queryset = Informations.objects.all()
    serializer_class = InformationsSerializer

    def retrieve(self, request, pk):
        infa = Informations.objects.get(id=pk)
        inf = InformationsSerializer(infa)
        return Response(inf.data)
        

class ProjectsView(ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    def list(self, request):
        project = Projects.objects.all()
        proj = ProjectsSerializer(project, many=True)
        return Response(proj.data)
        

class ContactsView(ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

    def list(self, request):
        project = Contacts.objects.last()
        proj = ContactsSerializer(project, )
        return Response(proj.data)


class ContactUsView(CreateAPIView):
    queryset = ContactUS.objects.all()
    serializer_class = ContactUSSerializer

    def create(self, request):
        name = request.data['name']
        phone = request.data['phone']
        msg = request.data['msg']
        a = ContactUS.objects.create(
            name=name,
            phone=phone,
            msg=msg
        )
        b = ContactUSSerializer(a)
        return Response(b.data)


class GrafikView(RetrieveAPIView):
    queryset = Grafik.objects.all()
    serializer_class = GrafikSerializer

    def retrieve(self, request, pk):
        infa = Grafik.objects.get(id=pk)
        inf = GrafikSerializer(infa)
        return Response(inf.data)
    

class MaqsadliAuditoriyaView(ListAPIView):
    queryset = MaqsadliAuditoriya.objects.all()
    serializer_class = MaqsadliAuditoriyaSerializer

    def list(self, request):
        maqsad = MaqsadliAuditoriya.objects.all()[0:5]
        mas =  MaqsadliAuditoriyaSerializer(maqsad, many=True)
        return Response(mas.data)

class ProtsentView(ListAPIView):
    queryset = Protsent.objects.all()
    serializer_class = ProtsentSerializer

    def list(self, request):
        maqsad = Protsent.objects.all()[0:4]
        mas =  ProtsentSerializer(maqsad, many=True)
        return Response(mas.data)

class DCView(RetrieveAPIView):
    queryset = DC.objects.all()
    serializer_class = DCSerializer

    def retrieve(self, request, pk):
        infa = DC.objects.get(id=pk)
        inf = DCSerializer(infa)
        return Response(inf.data)


class MapView(ListAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

    def list(self, request):
        maqsad = Map.objects.last()
        mas =  MapSerializer(maqsad, many=True)
        return Response(mas.data)




class XizmatView(ListAPIView):
    queryset = Xizmat.objects.all()
    serializer_class = XizmatSerializer

    def list(self, request):
        maqsad = Xizmat.objects.all()
        mas =  XizmatSerializer(maqsad, many=True)
        return Response(mas.data)

class XizmatSendView(CreateAPIView):
    queryset = XizmatSend.objects.all()
    serializer_class = XizmatSendSerializer

    def create(self, request):
        xizmat = request.data['xizmat']
        a = XizmatSend.objects.create(
            xizmat=xizmat
        )
        b = XizmatSendSerializer(a)
        return Response(b.data)
        
        