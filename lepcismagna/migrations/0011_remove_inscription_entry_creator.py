# Generated by Django 4.2.5 on 2023-11-09 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lepcismagna', '0010_alter_user_groups_alter_user_user_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='entry_creator',
        ),
    ]
