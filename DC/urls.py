from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("slider/", SliderView.as_view()),
    path("slider/", AboutTexnoParkView.as_view()),
    path("slider/", InformationsView.as_view()),
    path("slider/", ProjectsView.as_view()),
    path("slider/", ContactsView.as_view()),
    path("slider/", ContactUsView.as_view()),
    path("slider/", GrafikView.as_view()),
    path("slider/", MaqsadliAuditoriyaView.as_view()),
    path("slider/", ProtsentView.as_view()),
    path("slider/", DCView.as_view()),
    path("slider/", MapView.as_view()),
    path("slider/", XizmatView.as_view()),
    path("slider/", XizmatSendView.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
