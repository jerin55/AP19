# Generated by Django 4.1.3 on 2023-03-03 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='pagefollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.TextField(blank=True, max_length=255)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_users', to=settings.AUTH_USER_MODEL)),
                ('to_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_page', to='network.page')),
            ],
        ),
    ]
