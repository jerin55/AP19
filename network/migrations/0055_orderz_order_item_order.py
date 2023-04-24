# Generated by Django 4.1.3 on 2023-04-24 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0054_remove_order_item_order_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=255, null=True)),
                ('Phone', models.CharField(max_length=12, null=True)),
                ('House', models.CharField(max_length=255, null=True)),
                ('Area', models.CharField(max_length=60, null=True)),
                ('Landmark', models.CharField(max_length=60, null=True)),
                ('Town', models.CharField(max_length=60, null=True)),
                ('State', models.CharField(max_length=60, null=True)),
                ('Zip', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order_item',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.orderz'),
        ),
    ]