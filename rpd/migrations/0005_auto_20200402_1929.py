# Generated by Django 2.1 on 2020-04-02 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpd', '0004_auto_20200401_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableofdisc',
            name='educator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
