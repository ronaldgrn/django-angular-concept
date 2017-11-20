from django.db import models

# Create your models here.
class ProofOfConcept(models.Model):
    name = models.CharField(max_length=100)
    data = models.TextField()
    image = models.FileField(upload_to='photos/')

