from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Model for user handling
class User(AbstractUser):
    dossier = models.ManyToManyField("Inscription", blank=True, related_name="dossiers")
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user_permissions', blank=True, help_text='Specific permissions for this user.', related_name='custom_user_permissions')

 # Primary model for inscriptions   
class Inscription(models.Model):
    entry_creation_time = models.DateTimeField(auto_now_add=True)
    is_validated = models.BooleanField(default=False)
    reference_id = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    text = models.TextField(blank=True)
    letters = models.TextField(blank=True)
    date = models.CharField(max_length=50)
    findspot_desc = models.TextField(blank=True)
    associated_inscr = models.ManyToManyField('self')
    original_location = models.CharField(max_length=255)
    last_recorded_location = models.CharField(max_length=255)
    category = models.ManyToManyField('Category', blank=True)
    transcription_interpretive = models.TextField(blank=True)
    transcription_diplomatic = models.TextField(blank=True)
    transcription_appcrit = models.TextField(blank=True)
    translation_english = models.TextField(blank=True)
    commentary = models.TextField(blank=True)
    bibliography_text = models.TextField(blank=True)
    bibliography_entries = models.ManyToManyField('Bibliography', blank=True)
    abbreviations = models.ManyToManyField('Abbreviation', blank=True)
    age_at_death = models.ManyToManyField('AgeAtDeath', blank=True)
    divine_sacred_beings = models.ManyToManyField('DivineSacredBeing', blank=True)
    emperors_imperial_family = models.ManyToManyField('EmperorImperialFamily', blank=True)
    erasures = models.ManyToManyField('Erasure', blank=True)
    findspots = models.ManyToManyField('Findspot', blank=True)
    fragments = models.ManyToManyField('Fragment', blank=True)
    organizations = models.ManyToManyField('Organization', blank=True)
    people = models.ManyToManyField('Person', blank=True)
    personal_names = models.ManyToManyField('PersonalName', blank=True)
    place_names = models.ManyToManyField('PlaceName', blank=True)
    symbols = models.ManyToManyField('Symbol', blank=True)
    words = models.ManyToManyField('Word', blank=True)


# Models for bibliography information handling
class Bibliography(models.Model):

    class Meta:
        verbose_name_plural = 'bibliographies'

    short_title = models.CharField(max_length=50, blank=True)
    entry = models.TextField(blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)
    

class InscriptionBibliography(models.Model):

    class Meta:
        verbose_name_plural = 'inscription bibliographies'

    inscriptions = models.ForeignKey('Inscription', on_delete=models.CASCADE)
    bibliography = models.ForeignKey('Bibliography', on_delete=models.CASCADE)
    page_number_references = models.CharField(max_length=50)

class EpigraphicReference(models.Model):
    short_title = models.CharField(max_length=50, blank=True)
    entry = models.TextField(blank=True)
    inscriptions = models.ManyToManyField('Inscription', through='InscriptionReference', blank=True)

# Through model connecting Inscription and EpigraphicReference
class InscriptionReference(models.Model):
    inscription = models.ForeignKey('Inscription', on_delete=models.CASCADE)
    reference = models.ForeignKey('EpigraphicReference', on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=20, blank=True)


# Model for category handling
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# Model for image handling
class Image(models.Model):
    inscription_id = models.ForeignKey('Inscription', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True)


# Models for index handling
class Abbreviation(models.Model):
    abbreviation = models.CharField(max_length=20, blank=True)
    expansion = models.CharField(max_length=50, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

class AgeAtDeath(models.Model):

    class Meta:
        verbose_name_plural = 'ages at death'

    age = models.CharField(max_length=50, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

class DivineSacredBeing(models.Model):

    class Meta:
        verbose_name_plural = 'divine and sacred beings'

    divine_being = models.CharField(max_length=50, blank=True)
    epithet = models.CharField(max_length=50, blank=True)
    external_resource = models.URLField(max_length=255, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

class EmperorImperialFamily(models.Model):

    class Meta:
        verbose_name_plural = 'emperors and imperial families'

    person = models.CharField(max_length=50, blank=True)
    epithet = models.CharField(max_length=50, blank=True)
    external_resource = models.URLField(max_length=255, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

class Erasure(models.Model):
    erased_text = models.TextField(blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

class Findspot(models.Model):
    findspots_upper = models.CharField(max_length=255, blank=True)
    findspots_intermediate = models.CharField(max_length=255, blank=True)
    findspots_lower = models.CharField(max_length=255, blank=True)
    gazetteer = models.URLField(max_length=255, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

class Fragment(models.Model):
    fragment = models.CharField(max_length=50, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

class Organization(models.Model):
    name = models.CharField(max_length=50, blank=True)
    epithets = models.CharField(max_length=50, blank=True)
    external_resource = models.URLField(max_length=255, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

class Person(models.Model):

    class Meta:
        verbose_name_plural = 'people'

    person = models.CharField(max_length=100, blank=True)
    external_resource = models.CharField(max_length=255, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

class PersonalName(models.Model):
    name = models.CharField(max_length=50, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

class PlaceName(models.Model):
    place_name = models.CharField(max_length=100, blank=True)
    attested_form = models.CharField(max_length=100, blank=True)
    toponym_ethnic = models.CharField(max_length=10, blank=True)
    external_resource = models.URLField(max_length=255, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

class Symbol(models.Model):
    symbol = models.CharField(max_length=20, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

class Word(models.Model):
    lemma = models.CharField(max_length=20, blank=True)
    language_code = models.CharField(max_length=2, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)