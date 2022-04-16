# Generated by Django 4.0.3 on 2022-04-16 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lostfound', '0016_remove_item_lost_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='lost_by',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='lost', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
