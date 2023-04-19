# Generated by Django 4.1.3 on 2023-04-04 08:59

from django.db import migrations, models
import network.validators


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0023_rename_offer_price_post_offer_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Offer_price',
            new_name='offer_price',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Offer_End_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Offer_start_date',
        ),
        migrations.AddField(
            model_name='post',
            name='page_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default=True, max_length=130),
        ),
        migrations.AddField(
            model_name='post',
            name='vedio',
            field=models.FileField(blank=True, default=True, upload_to='posts/', validators=[network.validators.file_size]),
        ),
    ]