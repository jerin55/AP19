# Generated by Django 4.1.3 on 2023-04-25 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0058_orderz_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='ReviewReply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ReviewReply', to='network.reviewreply'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='network.review'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='type',
            field=models.CharField(choices=[('Default', 'Default'), ('User_Fllow', 'User_Fllow'), ('User_Fllowing', 'User_Fllowing'), ('User_Post_like', 'User_Post_like'), ('User_New_Post', 'User_New_Post'), ('User_Post_Reviwes', 'User_Post_Reviwes'), ('User_Post_Reviwes_Replay', 'User_Post_Reviwes_Replay'), ('Page_Invitions_To_User', 'Page_Invitions_To_User'), ('User_Accept_Page_Invitions', 'User_Accept_Page_Invitions'), ('User_Page_Join_Request', 'User_Page_Join_Request'), ('Page_Accept_User_Invitions', 'Page_Accept_User_Invitions'), ('Page_New_Post', 'Page_New_Post'), ('Page_Post_like', 'User_Post_like'), ('Page_Post_Reviwes', 'User_Post_Reviwes'), ('Page_Post_Reviwes_Replay', 'Page_Post_Reviwes_Replay'), ('Intrest_Post_Reviwes', 'Intrest_Post_Reviwes'), ('Intrest_Post_Reviwes_Replay', 'Intrest_Post_Reviwes_Replay'), ('Intrest_level_2_Post_Reviwes', 'Intrest_level_2_Post_Reviwes'), ('Intrest_level_2_Post_Reviwes_Replay', 'Intrest_level_2_Post_Reviwes_Replay')], default='Default', max_length=150),
        ),
    ]
