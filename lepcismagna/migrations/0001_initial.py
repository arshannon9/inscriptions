# Generated by Django 4.2.5 on 2023-11-07 15:12

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abbreviation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(blank=True, max_length=255)),
                ('expansion', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AgeAtDeath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Bibliography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_title', models.CharField(blank=True, max_length=255)),
                ('entry', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='DivineSacredBeing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divine_being', models.CharField(blank=True, max_length=255)),
                ('epithet', models.CharField(blank=True, max_length=255)),
                ('external_resource', models.URLField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EmperorImperialFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(blank=True, max_length=255)),
                ('epithet', models.CharField(blank=True, max_length=255)),
                ('external_resource', models.URLField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EpigraphicReference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_title', models.CharField(blank=True, max_length=255)),
                ('entry', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Erasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erased_text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Findspot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('findspots_upper', models.CharField(blank=True, max_length=255)),
                ('findspots_intermediate', models.CharField(blank=True, max_length=255)),
                ('findspots_lower', models.CharField(blank=True, max_length=255)),
                ('gazetteer', models.URLField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Fragment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fragment', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_creation_time', models.DateTimeField(auto_now_add=True)),
                ('is_validated', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('text', models.TextField(blank=True)),
                ('letters', models.TextField(blank=True)),
                ('date', models.CharField(max_length=255)),
                ('findspot_desc', models.TextField(blank=True)),
                ('original_location', models.CharField(max_length=255)),
                ('last_recorded_location', models.CharField(max_length=255)),
                ('transcription_interpretive', models.TextField(blank=True)),
                ('transcription_diplomatic', models.TextField(blank=True)),
                ('transcription_appcrit', models.TextField(blank=True)),
                ('translation_english', models.TextField(blank=True)),
                ('commentary', models.TextField(blank=True)),
                ('bibliography_text', models.TextField(blank=True)),
                ('abbreviations', models.ManyToManyField(blank=True, to='lepcismagna.abbreviation')),
                ('age_at_death', models.ManyToManyField(blank=True, to='lepcismagna.ageatdeath')),
                ('associated_inscr', models.ManyToManyField(to='lepcismagna.inscription')),
                ('bibliography_entries', models.ManyToManyField(blank=True, to='lepcismagna.bibliography')),
                ('category', models.ManyToManyField(blank=True, to='lepcismagna.category')),
                ('divine_sacred_beings', models.ManyToManyField(blank=True, to='lepcismagna.divinesacredbeing')),
                ('emperors_imperial_family', models.ManyToManyField(blank=True, to='lepcismagna.emperorimperialfamily')),
                ('erasures', models.ManyToManyField(blank=True, to='lepcismagna.erasure')),
                ('findspots', models.ManyToManyField(blank=True, to='lepcismagna.findspot')),
                ('fragments', models.ManyToManyField(blank=True, to='lepcismagna.fragment')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('epithets', models.CharField(blank=True, max_length=255)),
                ('external_resource', models.URLField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(blank=True, max_length=255)),
                ('external_resource', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(blank=True, max_length=255)),
                ('attested_form', models.CharField(blank=True, max_length=255)),
                ('toponym_ethnic', models.CharField(blank=True, max_length=255)),
                ('external_resource', models.URLField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lemma', models.CharField(blank=True, max_length=255)),
                ('language_code', models.CharField(blank=True, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('dossier', models.ManyToManyField(blank=True, related_name='dossiers', to='lepcismagna.inscription')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_user_groups', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_permissions', to='auth.permission', verbose_name='user_permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='InscriptionReference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(blank=True, max_length=255)),
                ('inscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.inscription')),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.epigraphicreference')),
            ],
        ),
        migrations.CreateModel(
            name='InscriptionBibliography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_number_references', models.CharField(max_length=255)),
                ('bibliography', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.bibliography')),
                ('inscriptions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.inscription')),
            ],
        ),
        migrations.AddField(
            model_name='inscription',
            name='organizations',
            field=models.ManyToManyField(blank=True, to='lepcismagna.organization'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='people',
            field=models.ManyToManyField(blank=True, to='lepcismagna.person'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='personal_names',
            field=models.ManyToManyField(blank=True, to='lepcismagna.personalname'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='place_names',
            field=models.ManyToManyField(blank=True, to='lepcismagna.placename'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='symbols',
            field=models.ManyToManyField(blank=True, to='lepcismagna.symbol'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='words',
            field=models.ManyToManyField(blank=True, to='lepcismagna.word'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('inscription_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.inscription')),
            ],
        ),
        migrations.AddField(
            model_name='epigraphicreference',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, through='lepcismagna.InscriptionReference', to='lepcismagna.inscription'),
        ),
    ]
