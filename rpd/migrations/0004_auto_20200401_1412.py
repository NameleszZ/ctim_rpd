# Generated by Django 2.1 on 2020-04-01 09:12

from django.db import migrations
import rpd.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rpd', '0003_auto_20200401_1337'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tableofdisc',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='tableofdisc',
            name='order',
            field=rpd.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
