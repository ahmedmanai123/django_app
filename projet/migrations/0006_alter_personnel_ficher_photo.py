# Generated by Django 4.1.7 on 2023-04-30 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0005_service_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='ficher_photo',
            field=models.ImageField(upload_to='images/personnel'),
        ),
    ]
