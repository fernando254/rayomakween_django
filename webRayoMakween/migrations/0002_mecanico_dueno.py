# Generated by Django 3.2.5 on 2021-07-14 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webRayoMakween', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mecanico',
            name='dueno',
            field=models.CharField(default='--', max_length=45),
        ),
    ]
