# Generated by Django 5.0.6 on 2024-06-08 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favsapp', '0002_alter_sites_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='sites',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/'),
        ),
    ]
