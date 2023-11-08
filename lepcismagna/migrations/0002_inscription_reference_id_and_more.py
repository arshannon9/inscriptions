# Generated by Django 4.2.5 on 2023-11-08 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lepcismagna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='reference_id',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='abbreviation',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='abbreviation',
            name='expansion',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='ageatdeath',
            name='age',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='bibliography',
            name='short_title',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='divinesacredbeing',
            name='divine_being',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='divinesacredbeing',
            name='epithet',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='emperorimperialfamily',
            name='epithet',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='emperorimperialfamily',
            name='person',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='epigraphicreference',
            name='short_title',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='fragment',
            name='fragment',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='inscriptionbibliography',
            name='page_number_references',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='inscriptionreference',
            name='reference_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='organization',
            name='epithets',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='person',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='personalname',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='placename',
            name='attested_form',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='placename',
            name='place_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='placename',
            name='toponym_ethnic',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='symbol',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='word',
            name='lemma',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
