# Generated by Django 3.2.9 on 2021-12-07 05:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='query',
            name='expiry',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
