from django.db import models

# Create your models here.


class Show(models.Model):
    show_name = models.CharField(max_length=50)
    show_url = models.URLField(max_length=300)
    latest_episode_url = models.URLField(max_length=400)
    latest_episode_name = models.CharField(max_length=100, null=True, blank=True)
    latest_post_time = models.CharField(max_length=50, null=True, blank=True)
    refreshed_time = models.DateTimeField(null=True, blank=True)
    show_image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.show_name
