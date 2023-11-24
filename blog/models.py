from django.db import models


class Project_blog(models.Model):
    title = models.CharField(max_length=200)
    datatime =  models.TextField()
    description = models.CharField(max_length=250)


