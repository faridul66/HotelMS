# Generated by Django 3.0.4 on 2020-03-08 12:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcustomer',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
