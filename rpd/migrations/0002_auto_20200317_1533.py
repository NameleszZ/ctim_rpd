# Generated by Django 2.1 on 2020-03-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chairs',
            name='slug',
            field=models.SlugField(default=0, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialisations',
            name='slug',
            field=models.SlugField(default=0, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tableofeducators',
            name='slug',
            field=models.SlugField(default=0, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tableofdisc',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
