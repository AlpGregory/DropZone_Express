# Generated by Django 4.2.4 on 2023-09-29 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_alter_client_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='birthday',
        ),
    ]
