# Generated by Django 4.0.1 on 2022-01-30 05:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_publicchatmessage_publicchatroom_remove_room_host_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicchatroom',
            name='host',
        ),
        migrations.AlterField(
            model_name='publicchatroom',
            name='users',
            field=models.ManyToManyField(blank=True, help_text='users conected', to=settings.AUTH_USER_MODEL),
        ),
    ]
