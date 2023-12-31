# Generated by Django 4.2.5 on 2023-11-08 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lepcismagna', '0005_abbreviation_inscriptions_ageatdeath_inscriptions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abbreviation',
            name='inscriptions',
        ),
        migrations.CreateModel(
            name='InscriptionAbbreviation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_number_reference', models.CharField(blank=True, max_length=50)),
                ('abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.abbreviation')),
                ('inscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.inscription')),
            ],
        ),
        migrations.AddField(
            model_name='abbreviation',
            name='inscription_references',
            field=models.ManyToManyField(blank=True, through='lepcismagna.InscriptionAbbreviation', to='lepcismagna.inscription'),
        ),
    ]
