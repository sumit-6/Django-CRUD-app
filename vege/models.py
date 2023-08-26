from django.db import models

# Create your models here.
class Receipe(models.Model):
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.FileField(upload_to="recipe")
    
