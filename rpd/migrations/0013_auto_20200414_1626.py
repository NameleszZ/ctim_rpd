# Generated by Django 2.2.12 on 2020-04-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpd', '0012_auto_20200414_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableofdisc',
            name='status',
            field=models.CharField(choices=[('Новое', 'Новое'), ('Отправлено', 'Отправлено'), ('Одобрено', 'Одобрено'), ('На доработку', 'На доработку')], default='new', max_length=50, verbose_name='статус'),
        ),
    ]