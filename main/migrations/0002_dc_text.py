# Generated by Django 3.2.9 on 2022-05-03 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dc',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
