# Generated by Django 4.1.3 on 2023-04-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0022_post_lev2_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='offer_price',
            new_name='Offer_price',
        ),
        migrations.RemoveField(
            model_name='post',
            name='page_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='vedio',
        ),
        migrations.AddField(
            model_name='post',
            name='Offer_End_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Offer_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
