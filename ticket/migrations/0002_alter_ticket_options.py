# Generated by Django 3.2.5 on 2021-07-31 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ('-Time_created',)},
        ),
    ]