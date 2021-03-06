# Generated by Django 3.2.9 on 2022-05-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTexnoPark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('fa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='Contacts/')),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='DC/')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='DC/')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='DC/')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='DC/')),
                ('img5', models.ImageField(blank=True, null=True, upload_to='DC/')),
                ('img6', models.ImageField(blank=True, null=True, upload_to='DC/')),
            ],
        ),
        migrations.CreateModel(
            name='Grafik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Informations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Informations/')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=50)),
                ('end', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MaqsadliAuditoriya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=300)),
                ('img', models.ImageField(upload_to='MaqsadliAuditoriya/')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='Projects/')),
                ('link', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Protsent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('protsent', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Slider/')),
                ('video', models.FileField(upload_to='Slider/')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Xizmat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
