# Generated by Django 3.2.9 on 2021-12-07 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211207_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='query',
            name='expiry',
            field=models.DateTimeField(),
        ),
    ]
