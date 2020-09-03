# Generated by Django 3.0.4 on 2020-07-02 01:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0004_roombooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoundryBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_number', models.CharField(max_length=20)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('r_cost', models.IntegerField()),
                ('r_description', models.TextField()),
            ],
        ),
    ]