# Generated by Django 3.1.2 on 2021-08-24 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210823_2159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at']},
        ),
    ]
