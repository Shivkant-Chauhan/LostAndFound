# Generated by Django 4.0.3 on 2022-04-15 19:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lostfound', '0011_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='hotel_Main_Img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
