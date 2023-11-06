from django.db import models

# Create your models here.

 # Primary model for inscriptions   
class Inscription(models.Model):
    entry_creation_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    text = models.TextField(blank=True)
    letters = models.TextField(blank=True)
    date = models.CharField(max_length=255)
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
    findspots = models.ManyToManyField('Findspot', blank=True)

# Models for bibliography information handling
class Bibliography(models.Model):
    short_title = models.CharField(max_length=255, blank=True)
    entry = models.TextField(blank=True)

class InscriptionBibliography(models.Model):
    inscription = models.ForeignKey('Inscription', on_delete=models.CASCADE)
    bibliography = models.ForeignKey('Bibliography', on_delete=models.CASCADE)
    page_number_references = models.CharField(max_length=255)

# Model for category handling
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
# Model for image handling
class Image(models.Model):
    inscription_id = models.ForeignKey('Inscription', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True)


# Models for index handling
class Abbreviation(models.Model):
    name = models.CharField(max_length=255)

class Findspot(models.Model):
    name = models.CharField(max_length=255, blank=True)



