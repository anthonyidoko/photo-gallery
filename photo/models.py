from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name

class Picture(models.Model):
    category = models.ForeignKey("Category", on_delete = models.CASCADE)
    image = models.ImageField(upload_to = "pictures")
    description = models.CharField(max_length = 2000)
    date_added = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return self.description