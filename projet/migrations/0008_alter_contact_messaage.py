# Generated by Django 4.1.7 on 2023-05-02 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0007_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='messaage',
            field=models.TextField(max_length=500),
        ),
    ]
