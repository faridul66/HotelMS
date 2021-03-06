# Generated by Django 3.0.4 on 2020-03-08 16:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0002_addcustomer_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_number', models.IntegerField()),
                ('r_cost', models.IntegerField()),
                ('r_type', models.CharField(max_length=20)),
                ('r_description', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
