# Generated by Django 4.1.3 on 2023-03-30 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0016_remove_user_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
    ]
