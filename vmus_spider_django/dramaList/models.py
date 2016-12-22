from django.db import models

# Create your models here.


class Show(models.Model):
    show_name = models.CharField(max_length=50)
    show_url = models.URLField()
    latest_episode_url = models.URLField()
    latest_episode_name = models.CharField(max_length=100, null=True, blank=True)
    latest_post_time = models.CharField(max_length=50, null=True, blank=True)
    show_image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.show_name
