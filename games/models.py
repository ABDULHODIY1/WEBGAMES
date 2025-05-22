from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    iframe_url = models.URLField()
    cover_image = models.ImageField(upload_to='covers/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
