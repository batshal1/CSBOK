# Generated by Django 3.2.7 on 2021-09-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csbok', '0003_topic_video_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='video_link',
            field=models.TextField(blank=True),
        ),
    ]
