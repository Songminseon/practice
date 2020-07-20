from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=50)
    date = models.DateField('date published')
    body = models.TextField()
    img = models.ImageField(upload_to="images/", blank="True")

    def __str__(self):
        return self.title
# Create your models here.
