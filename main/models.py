from django.db import models

class Slider(models.Model):
    img = models.ImageField(upload_to="Slider/")
    video = models.FileField(upload_to="Slider/")
    title = models.CharField(max_length=200)

class AboutTexnoPark(models.Model):
    title = models.CharField(max_length=50)
    number = models.IntegerField()
    fa = models.CharField(max_length=100)

class Informations(models.Model):
    img = models.ImageField(upload_to="Informations/")
    text = models.TextField()

class Projects(models.Model):
    img = models.FileField(upload_to="Projects/")
    link = models.CharField(max_length=500)

class Contacts(models.Model):
    logo = models.ImageField(upload_to="Contacts/")
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

class ContactUS(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    msg = models.TextField()

class Grafik(models.Model):
    text = models.TextField()

class MaqsadliAuditoriya(models.Model):
    title = models.CharField(max_length=100) 
    text = models.CharField(max_length=300) 
    img = models.ImageField(upload_to="MaqsadliAuditoriya/")

class Protsent(models.Model):
    name = models.CharField(max_length=100)
    protsent = models.CharField(max_length=10)

class DC(models.Model):
    img1 = models.ImageField(upload_to="DC/")
    img2 = models.ImageField(upload_to="DC/", blank=True, null=True)
    img3 = models.ImageField(upload_to="DC/", blank=True, null=True)
    img4 = models.ImageField(upload_to="DC/", blank=True, null=True)
    img5 = models.ImageField(upload_to="DC/", blank=True, null=True)
    img6 = models.ImageField(upload_to="DC/", blank=True, null=True)
    text = models.TextField()

class Map(models.Model):
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    
class Xizmat(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    price = models.IntegerField()

class XizmatSend(models.Model):
    xizmat = models.ForeignKey(Xizmat, on_delete=models.CASCADE)

    