from django.db import models

# Create your models here.
class Diseases(models.Model):
    diseases = models.CharField(max_length = 20)
    
    def __unicode__(self):
        return self.diseases

class Symptoms(models.Model):
    disease = models.ForeignKey(Diseases)
    symptoms = models.CharField(max_length = 20)
    
    
    def __unicode__(self):
        return self.symptoms