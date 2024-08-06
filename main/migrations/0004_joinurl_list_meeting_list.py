# Generated by Django 2.2.6 on 2022-07-12 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_joinurl_list_meeting_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='joinurl_list',
            name='meeting_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Meeting_details'),
            preserve_default=False,
        ),
    ]