# Generated by Django 3.2.5 on 2021-07-31 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='publish',
        ),
        migrations.RemoveField(
            model_name='review',
            name='status',
        ),
        migrations.RemoveField(
            model_name='review',
            name='updated',
        ),
    ]