from django.db import models

class Video(models.Model):
    caption=models.CharField(max_length=100)
    Description=models.TextField()
    video=models.FileField(upload_to='videos/')

    def __str__(self):
        return self.caption
