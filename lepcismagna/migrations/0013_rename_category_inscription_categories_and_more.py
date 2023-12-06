# Generated by Django 4.2.7 on 2023-12-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lepcismagna', '0012_remove_image_inscription_id_image_reference_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscription',
            old_name='category',
            new_name='categories',
        ),
        migrations.AddField(
            model_name='category',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, to='lepcismagna.inscription'),
        ),
    ]
