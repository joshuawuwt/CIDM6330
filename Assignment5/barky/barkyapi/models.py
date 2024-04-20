from django.db import models

# Create your models here.
class Bookmark(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    url = models.URLField()
    notes = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"