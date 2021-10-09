from django.db import models

# Create your models here.

class Simulation_Project(models.Model):
    project_id = models.AutoField
    project_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    geogebra_link = models.CharField(max_length=1000)
    youtube_link = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images' , null=True)

    def __str__(self):
        return self.project_name

class Video_Project(models.Model):
    project_id = models.AutoField
    project_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    youtube_link = models.CharField(max_length=1000)


    def __str__(self):
        return self.project_name