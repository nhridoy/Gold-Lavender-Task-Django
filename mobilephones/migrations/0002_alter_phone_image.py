# Generated by Django 4.0 on 2021-12-25 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobilephones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(blank=True, default='phone/default.png', upload_to='phone/'),
        ),
    ]