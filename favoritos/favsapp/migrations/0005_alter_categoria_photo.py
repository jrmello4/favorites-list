# Generated by Django 5.0.6 on 2024-06-08 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favsapp', '0004_remove_sites_photo_categoria_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
